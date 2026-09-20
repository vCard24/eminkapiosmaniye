#!/usr/bin/env node
/**
 * Inject shared topbar/header/footer from partials/ into content HTML pages.
 * Usage: node scripts/inject-chrome.mjs
 *
 * - Skips redirect stubs
 * - Replaces {{ROOT}} with "" or "../" by depth
 * - Sets aria-current="page" on matching nav links
 * - Wraps chrome in <!-- chrome:*:start/end --> markers for re-runs
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = path.resolve(__dirname, "..");
const PARTIALS = path.join(ROOT_DIR, "partials");

const MARKERS = {
  topbar: { start: "<!-- chrome:topbar:start -->", end: "<!-- chrome:topbar:end -->" },
  header: { start: "<!-- chrome:header:start -->", end: "<!-- chrome:header:end -->" },
  footer: { start: "<!-- chrome:footer:start -->", end: "<!-- chrome:footer:end -->" },
};

function readPartial(name) {
  return fs.readFileSync(path.join(PARTIALS, name), "utf8").replace(/\r\n/g, "\n").trimEnd();
}

function walkHtmlFiles(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "node_modules" || entry.name === "partials" || entry.name === "katalog-flip") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walkHtmlFiles(full, out);
    else if (entry.isFile() && entry.name.endsWith(".html")) out.push(full);
  }
  return out;
}

function isRedirectStub(html) {
  const hasChrome = /class="site-header"/.test(html);
  if (hasChrome) return false;
  return (
    /location\.replace\s*\(/.test(html) ||
    /http-equiv\s*=\s*["']refresh["']/i.test(html) ||
    (/noindex/i.test(html) && /Yönlendiriliyor/i.test(html))
  );
}

function sitePathFromFile(absFile) {
  return path.relative(ROOT_DIR, absFile).split(path.sep).join("/");
}

function rootPrefix(sitePath) {
  const depth = sitePath.split("/").length - 1;
  return depth > 0 ? "../".repeat(depth) : "";
}

function normalizeHref(href, pageDir) {
  if (!href || href.startsWith("tel:") || href.startsWith("mailto:") || href.startsWith("http") || href.startsWith("#")) {
    return null;
  }
  // Resolve relative to page directory → site-root relative
  const joined = path.posix.normalize(path.posix.join(pageDir || ".", href));
  return joined.replace(/^\.\//, "");
}

function applyAriaCurrent(chromeHtml, sitePath) {
  const pageDir = path.posix.dirname(sitePath);
  const pageKey = sitePath;

  // Remove any existing aria-current
  let out = chromeHtml.replace(/\s+aria-current="page"/g, "");

  // Match <a ... href="..."> and add aria-current when href resolves to this page
  out = out.replace(/<a\b([^>]*?)>/g, (full, attrs) => {
    if (/\bclass="[^"]*\blogo-link\b/.test(attrs)) return full;
    const hrefMatch = attrs.match(/\bhref="([^"]*)"/);
    if (!hrefMatch) return full;
    const href = hrefMatch[1];
    // href already has ROOT substituted; resolve from page dir
    const resolved = normalizeHref(href, pageDir);
    if (!resolved || resolved !== pageKey) return full;
    if (/\baria-current=/.test(attrs)) return full;
    return `<a${attrs} aria-current="page">`;
  });

  return out;
}

function wrap(name, body) {
  const m = MARKERS[name];
  return `${m.start}\n${body}\n${m.end}`;
}

function replaceMarkedOrLegacy(html, name, wrapped) {
  const m = MARKERS[name];
  const marked = new RegExp(
    `${escapeRe(m.start)}[\\s\\S]*?${escapeRe(m.end)}`,
    "m"
  );
  if (marked.test(html)) {
    return html.replace(marked, wrapped);
  }

  if (name === "topbar") {
    const re = /<div class="topbar">[\s\S]*?(?=<header class="site-header">)/;
    if (!re.test(html)) throw new Error("topbar not found");
    return html.replace(re, `${wrapped}\n\n  `);
  }
  if (name === "header") {
    const re = /<header class="site-header">[\s\S]*?<\/header>/;
    if (!re.test(html)) throw new Error("header not found");
    return html.replace(re, wrapped);
  }
  if (name === "footer") {
    const re = /<footer class="site-footer">[\s\S]*?<\/footer>/;
    if (!re.test(html)) throw new Error("footer not found");
    return html.replace(re, wrapped);
  }
  return html;
}

function escapeRe(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function ensureDataRoot(html, root) {
  // Set data-root on <html ...>
  if (/<html\b[^>]*\bdata-root=/.test(html)) {
    return html.replace(/(<html\b[^>]*\bdata-root=")[^"]*(")/, `$1${root}$2`);
  }
  return html.replace(/<html\b([^>]*)>/, `<html$1 data-root="${root}">`);
}

function renderPartial(template, root) {
  return template.replaceAll("{{ROOT}}", root);
}

function processFile(absFile, partials) {
  const sitePath = sitePathFromFile(absFile);
  let html = fs.readFileSync(absFile, "utf8").replace(/\r\n/g, "\n");

  if (isRedirectStub(html)) {
    return { sitePath, status: "skipped-stub" };
  }

  if (!/class="site-header"/.test(html) && !html.includes(MARKERS.header.start)) {
    return { sitePath, status: "skipped-no-chrome" };
  }

  const root = rootPrefix(sitePath);
  const topbar = renderPartial(partials.topbar, root);
  let header = renderPartial(partials.header, root);
  let footer = renderPartial(partials.footer, root);
  header = applyAriaCurrent(header, sitePath);
  footer = applyAriaCurrent(footer, sitePath);

  html = replaceMarkedOrLegacy(html, "topbar", wrap("topbar", topbar));
  html = replaceMarkedOrLegacy(html, "header", wrap("header", header));
  html = replaceMarkedOrLegacy(html, "footer", wrap("footer", footer));
  html = ensureDataRoot(html, root);

  fs.writeFileSync(absFile, html.endsWith("\n") ? html : html + "\n", "utf8");
  return { sitePath, status: "updated", root };
}

function main() {
  const partials = {
    topbar: readPartial("topbar.html"),
    header: readPartial("header.html"),
    footer: readPartial("footer.html"),
  };

  const files = walkHtmlFiles(ROOT_DIR);
  const results = { updated: 0, skippedStub: 0, skippedOther: 0, errors: [] };

  for (const file of files) {
    try {
      const r = processFile(file, partials);
      if (r.status === "updated") {
        results.updated++;
        console.log(`✓ ${r.sitePath} (ROOT="${r.root}")`);
      } else if (r.status === "skipped-stub") {
        results.skippedStub++;
        console.log(`· skip stub  ${r.sitePath}`);
      } else {
        results.skippedOther++;
        console.log(`· skip       ${r.sitePath}`);
      }
    } catch (err) {
      results.errors.push({ file, err: String(err.message || err) });
      console.error(`✗ ${sitePathFromFile(file)}: ${err.message || err}`);
    }
  }

  console.log(
    `\nDone. updated=${results.updated} stubs=${results.skippedStub} other=${results.skippedOther} errors=${results.errors.length}`
  );
  if (results.errors.length) process.exitCode = 1;
}

main();
