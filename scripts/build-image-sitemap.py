#!/usr/bin/env python3
"""Build sitemap-images.xml from og:image + catalog gallery thumbs."""

from pathlib import Path
import re
from datetime import date
from urllib.parse import urljoin

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
        return f"{BASE}/{rel[:-10]}"
    return f"{BASE}/{rel}"


def xml_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def abs_img(src: str, page_rel: str) -> str | None:
    if not src or src.startswith("data:"):
        return None
    if src.startswith("http://") or src.startswith("https://"):
        return src
    page_dir = str(Path(page_rel).parent).replace("\\", "/")
    if page_dir == ".":
        base = f"{BASE}/"
    else:
        base = f"{BASE}/{page_dir}/"
    return urljoin(base, src)


def collect_images(text: str, page_rel: str) -> list[tuple[str, str]]:
    """Return ordered unique (image_url, title) for a page."""
    found: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(url: str | None, title: str) -> None:
        if not url or url in seen:
            return
        seen.add(url)
        found.append((url, (title or "Emin Kapı")[:120]))

    title_m = re.search(r"<title>([^<]+)</title>", text, flags=re.I)
    page_title = title_m.group(1).strip() if title_m else "Emin Kapı"

    og = re.search(r'property="og:image"\s+content="([^"]+)"', text)
    if not og:
        og = re.search(r'content="([^"]+)"\s+property="og:image"', text)
    if og:
        add(og.group(1), page_title)

    # Catalog thumbs: data-src + data-code (product caption)
    for m in re.finditer(
        r'data-catalog-thumb[^>]*data-code="([^"]*)"[^>]*data-src="([^"]+)"|'
        r'data-catalog-thumb[^>]*data-src="([^"]+)"[^>]*data-code="([^"]*)"',
        text,
        flags=re.I,
    ):
        if m.group(2):
            code, src = m.group(1), m.group(2)
        else:
            src, code = m.group(3), m.group(4)
        add(abs_img(src, page_rel), code or page_title)

    # Fallback: any figure/img under products path with alt
    for m in re.finditer(
        r'<img[^>]+src="([^"]+/assets/img/products/[^"]+)"[^>]*(?:alt="([^"]*)")?',
        text,
        flags=re.I,
    ):
        add(abs_img(m.group(1), page_rel), m.group(2) or page_title)

    return found


def main() -> None:
    pages: list[tuple[str, list[tuple[str, str]]]] = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("katalog-flip/", "partials/")):
            continue
        text = p.read_text(encoding="utf-8")
        if is_stub(text):
            continue
        images = collect_images(text, rel)
        if not images:
            continue
        pages.append((page_url(rel), images))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        "<!-- Image sitemap: og:image + catalog / product gallery images -->",
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    img_count = 0
    for loc, images in pages:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        for img, title in images:
            lines.append("    <image:image>")
            lines.append(f"      <image:loc>{xml_escape(img)}</image:loc>")
            lines.append(f"      <image:title>{xml_escape(title)}</image:title>")
            lines.append("    </image:image>")
            img_count += 1
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    out = ROOT / "sitemap-images.xml"
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"wrote {out.name}: {len(pages)} urls, {img_count} images")


if __name__ == "__main__":
    main()
