#!/usr/bin/env python3
"""Build sitemap-images.xml from content page og:image tags."""

from pathlib import Path
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://eminkapiosmaniye.com"
TODAY = date.today().isoformat()


def is_stub(text: str) -> bool:
    return (
        ("location.replace" in text or 'http-equiv="refresh"' in text.lower())
        and "site-header" not in text
    )


def page_url(rel: str) -> str:
    if rel == "index.html":
        return f"{BASE}/"
    if rel.endswith("/index.html"):
        return f"{BASE}/{rel[:-10]}"  # urunler/ or rehber/
    return f"{BASE}/{rel}"


def main() -> None:
    entries = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("katalog-flip/", "partials/")):
            continue
        text = p.read_text(encoding="utf-8")
        if is_stub(text):
            continue
        m = re.search(r'property="og:image"\s+content="([^"]+)"', text)
        if not m:
            m = re.search(r'content="([^"]+)"\s+property="og:image"', text)
        if not m:
            continue
        img = m.group(1)
        title_m = re.search(r"<title>([^<]+)</title>", text, flags=re.I)
        title = (title_m.group(1).strip() if title_m else "Emin Kapı")[:120]
        entries.append((page_url(rel), img, title))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!-- Image sitemap for Google Discover / search thumbnails -->',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    for loc, img, title in entries:
        safe_title = (
            title.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append("    <image:image>")
        lines.append(f"      <image:loc>{img}</image:loc>")
        lines.append(f"      <image:title>{safe_title}</image:title>")
        lines.append("    </image:image>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    out = ROOT / "sitemap-images.xml"
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"wrote {out.name} with {len(entries)} urls")


if __name__ == "__main__":
    main()
