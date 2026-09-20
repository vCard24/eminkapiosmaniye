import fs from "node:fs";

function check(f, expectRoot, expectAria) {
  const h = fs.readFileSync(f, "utf8");
  const markers = ["topbar", "header", "footer"].every(
    (n) => h.includes(`chrome:${n}:start`) && h.includes(`chrome:${n}:end`)
  );
  const dr = (h.match(/data-root="([^"]*)"/) || [])[1];
  const aria = [...h.matchAll(/<a([^>]*aria-current="page"[^>]*)>/g)].map((m) => {
    const hm = m[1].match(/href="([^"]+)"/);
    return hm && hm[1];
  });
  const ok =
    markers &&
    dr === expectRoot &&
    expectAria.every((x) => aria.includes(x)) &&
    h.includes("<main");
  console.log(
    `${ok ? "PASS" : "FAIL"} ${f} | markers=${markers} data-root=${JSON.stringify(dr)} aria=${JSON.stringify(aria)}`
  );
  return ok;
}

let all = true;
all =
  check("index.html", "", ["index.html"]) &&
  check("katalog.html", "", ["katalog.html"]) &&
  check("urunler/celik-kapi.html", "../", ["../urunler/celik-kapi.html"]) &&
  check("rehber/osmaniye-oda-kapisi-fiyatlari.html", "../", [
    "../rehber/osmaniye-oda-kapisi-fiyatlari.html",
  ]) &&
  check("sikca-sorulan-sorular.html", "", ["sikca-sorulan-sorular.html"]) &&
  all;

const stub = fs.readFileSync("rehber/oda-kapisi-fiyatlari.html", "utf8");
const stubOk = !stub.includes("site-header") && stub.includes("location.replace");
console.log(`${stubOk ? "PASS" : "FAIL"} stub untouched`);
all = all && stubOk;

const kat = fs.readFileSync("katalog.html", "utf8");
const katOk =
  kat.includes("katalog-flip/vendor/pdf.min.js") &&
  kat.includes("katalog-flip/script.js");
console.log(`${katOk ? "PASS" : "FAIL"} katalog scripts intact`);
all = all && katOk;

process.exitCode = all ? 0 : 1;
