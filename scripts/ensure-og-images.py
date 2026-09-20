#!/usr/bin/env python3
"""Ensure every content page has a strong og:image + Product.image for Google thumbnails."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://eminkapiosmaniye.com"

MAP = {
    "index.html": "/assets/img/slider/emin_kapi_celik_kapi-04.webp",
    "iletisim.html": "/assets/img/emin-kapi-fabrika.png",
    "hakkimizda.html": "/assets/img/emin-kapi-fabrika.png",
    "katalog.html": "/assets/img/slider/emin_kapi_celik_kapi-04.webp",
    "sikca-sorulan-sorular.html": "/assets/img/products/cards/bilgi-fiyat-rehberi.webp",
    "gizlilik-politikasi.html": "/assets/img/emin-kapi-fabrika.png",
    "kvkk.html": "/assets/img/emin-kapi-fabrika.png",
    "kullanim-kosullari.html": "/assets/img/emin-kapi-fabrika.png",
    "urunler/index.html": "/assets/img/products/cards/ic-oda-kapisi.webp",
    "urunler/ic-oda-kapisi.html": "/assets/img/products/cards/ic-oda-kapisi.webp",
    "urunler/amerikan-panel.html": "/assets/img/products/cards/amerikan-panel.webp",
    "urunler/melamin-panel.html": "/assets/img/products/cards/melamin-panel.webp",
    "urunler/kompozit-panel.html": "/assets/img/products/cards/kompozit-panel.webp",
    "urunler/lake-kapi.html": "/assets/img/products/cards/lake-kapi.webp",
    "urunler/camli-ic-kapi.html": "/assets/img/products/cards/camli-ic-kapi.webp",
    "urunler/celik-kapi.html": "/assets/img/products/cards/celik-kapi.webp",
    "urunler/pvc-kapi-pencere.html": "/assets/img/products/pvc/pvc-agac-desenli-kapi.webp",
    "urunler/mobilya.html": "/assets/img/products/cards/mobilya.webp",
    "urunler/mutfak-dolabi.html": "/assets/img/products/mobilya/mutfak-dolabi/osmaniye-mutfak-dolabi.webp",
    "urunler/gardrop-yatak-odasi.html": "/assets/img/products/mobilya/cards/gardrop.webp",
    "urunler/portmanto.html": "/assets/img/products/mobilya/cards/portmanto.webp",
    "urunler/vestiyer.html": "/assets/img/products/mobilya/cards/vestiyer.webp",
    "urunler/banyo-dolabi.html": "/assets/img/products/mobilya/cards/banyo.webp",
    "urunler/villa-mobilyasi.html": "/assets/img/products/mobilya/cards/villa.webp",
    "urunler/laminant-parke.html": "/assets/img/products/mobilya/cards/parke.webp",
    "rehber/index.html": "/assets/img/products/cards/bilgi-fiyat-rehberi.webp",
    "rehber/osmaniye-oda-kapisi-fiyatlari.html": "/assets/img/products/cards/ic-oda-kapisi.webp",
    "rehber/osmaniye-oda-kapi-modelleri.html": "/assets/img/products/cards/amerikan-panel.webp",
    "rehber/osmaniye-ev-ic-kapi-modelleri-ve-fiyatlari.html": "/assets/img/products/cards/melamin-panel.webp",
    "rehber/osmaniye-lake-ic-kapi-modelleri-ve-fiyatlari.html": "/assets/img/products/cards/lake-kapi.webp",
    "rehber/osmaniye-luks-ic-kapi-modelleri.html": "/assets/img/products/cards/camli-ic-kapi.webp",
    "rehber/osmaniye-celik-kapi-fiyatlari.html": "/assets/img/products/cards/celik-kapi.webp",
    "rehber/osmaniye-celik-kapi-kilitleri.html": "/assets/img/products/celik-kilit/01-hafif-multisistem-merkezi-celik-kapi-kilidi.jpg",
    "rehber/osmaniye-mutfak-dolabi-fiyatlari.html": "/assets/img/products/cards/mobilya.webp",
    "rehber/osmaniye-en-cok-tercih-edilen-kapi-modelleri.html": "/assets/img/products/cards/kompozit-panel.webp",
    "rehber/osmaniye-kapi-fabrikalari.html": "/assets/img/emin-kapi-fabrika.png",
    "rehber/osmaniye-garanti-kosullari.html": "/assets/img/products/cards/bilgi-fiyat-rehberi.webp",
}

DEFAULT = "/assets/img/slider/emin_kapi_celik_kapi-04.webp"


def is_stub(text: str) -> bool:
    return (
        ("location.replace" in text or 'http-equiv="refresh"' in text.lower())
        and "site-header" not in text
    )


def ensure_robots(html: str) -> str:
    html = re.sub(
        r'<meta name="robots" content="index, follow"\s*/?>',
        '<meta name="robots" content="index, follow, max-image-preview:large" />',
        html,
        count=1,
        flags=re.I,
    )
    if "max-image-preview" in html:
        return html
    tag = '<meta name="robots" content="index, follow, max-image-preview:large" />\n  '
    m = re.search(r'<meta name="description"[^>]*>\s*', html, flags=re.I)
    if m:
        return html[: m.end()] + tag + html[m.end() :]
    m = re.search(r'<meta name="viewport"[^>]*>\s*', html, flags=re.I)
    if m:
        return html[: m.end()] + tag + html[m.end() :]
    return html


def upsert_og_image(html: str, abs_url: str, title_hint: str) -> str:
    alt = (title_hint or "Emin Kapı Osmaniye").replace('"', "")
    if re.search(r'property="og:image"', html):
        html = re.sub(
            r'<meta property="og:image"[^>]*>\s*',
            f'<meta property="og:image" content="{abs_url}" />\n  ',
            html,
            count=1,
        )
        if "og:image:alt" not in html:
            html = re.sub(
                r'(<meta property="og:image"[^>]*>)',
                rf'\1\n  <meta property="og:image:alt" content="{alt}" />',
                html,
                count=1,
            )
        else:
            html = re.sub(
                r'<meta property="og:image:alt"[^>]*>',
                f'<meta property="og:image:alt" content="{alt}" />',
                html,
                count=1,
            )
        if "twitter:card" not in html:
            html = re.sub(
                r'(<meta property="og:image"[^>]*>)',
                rf'\1\n  <meta name="twitter:card" content="summary_large_image" />',
                html,
                count=1,
            )
        if "twitter:image" not in html:
            html = re.sub(
                r'(<meta name="twitter:card"[^>]*>)',
                rf'\1\n  <meta name="twitter:image" content="{abs_url}" />',
                html,
                count=1,
            )
        else:
            html = re.sub(
                r'<meta name="twitter:image"[^>]*>',
                f'<meta name="twitter:image" content="{abs_url}" />',
                html,
                count=1,
            )
        return html

    block = (
        f'<meta property="og:image" content="{abs_url}" />\n'
        f'  <meta property="og:image:alt" content="{alt}" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:image" content="{abs_url}" />\n  '
    )
    m = re.search(r'<meta property="og:title"[^>]*>\s*', html)
    if m:
        return html[: m.end()] + block + html[m.end() :]
    m = re.search(r'<link rel="canonical"[^>]*>\s*', html)
    if m:
        return html[: m.end()] + block + html[m.end() :]
    m = re.search(r"</head>", html, flags=re.I)
    if m:
        return html[: m.start()] + "  " + block + html[m.start() :]
    return html


def add_product_image(html: str, abs_url: str) -> str:
    if '"@type": "Product"' not in html and '"@type":"Product"' not in html:
        return html

    # Skip if Product already has image within following ~900 chars
    m = re.search(r'"@type"\s*:\s*"Product"', html)
    if not m:
        return html
    window = html[m.start() : m.start() + 900]
    if re.search(r'"image"\s*:', window):
        # Replace simple string image if present right after Product name for consistency
        html2 = re.sub(
            r'("@type"\s*:\s*"Product",\s*\n\s*"name"\s*:\s*"[^"]+",\s*\n\s*"image"\s*:\s*")[^"]+(")',
            rf'\1{abs_url}\2',
            html,
            count=1,
        )
        return html2

    html2 = re.sub(
        r'("@type"\s*:\s*"Product",\s*\n\s*"name"\s*:\s*"[^"]+",)',
        rf'\1\n        "image": "{abs_url}",',
        html,
        count=1,
    )
    if html2 != html:
        return html2

    return re.sub(
        r'("@type"\s*:\s*"Product","name"\s*:\s*"[^"]+",)',
        rf'\1"image":"{abs_url}",',
        html,
        count=1,
    )


def main() -> None:
    updated = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith("katalog-flip/") or rel.startswith("partials/"):
            continue
        text = p.read_text(encoding="utf-8")
        if is_stub(text):
            continue
        img_path = MAP.get(rel, DEFAULT)
        abs_url = BASE + img_path
        title_m = re.search(r"<title>([^<]+)</title>", text, flags=re.I)
        title = (title_m.group(1).strip() if title_m else "Emin Kapı Osmaniye")[:90]
        new = ensure_robots(text)
        new = upsert_og_image(new, abs_url, title)
        new = add_product_image(new, abs_url)
        if new != text:
            p.write_text(new, encoding="utf-8", newline="\n")
            updated.append(rel)
    print(f"updated {len(updated)}")
    for u in updated:
        print(" -", u)


if __name__ == "__main__":
    main()
