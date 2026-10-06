# -*- coding: utf-8 -*-
"""Convert ekim job photos to webp and inject horizontal strips into product pages."""
from __future__ import annotations

import re
from html import escape
from pathlib import Path

from PIL import Image, ImageOps

SRC = Path(r"C:\Users\mosta\Desktop\Eminkapi_doneler\ekim")
ROOT = Path(r"C:\Users\mosta\Desktop\emin-kapi-full")
OUT_DIR = ROOT / "assets" / "img" / "products" / "mobilya" / "uygulamalar"
SITEMAP = ROOT / "sitemap-images.xml"
WEB_PREFIX = "../assets/img/products/mobilya/uygulamalar"
SKIP = {"cift-kanat-camli-ic-oda-kapisi", "ic-oda-oval-camli-kapi"}

TR = [
    ("yatak-odasi", "yatak odası"),
    ("amerikan-tarzi", "Amerikan tarzı"),
    ("ozel-tasarim", "özel tasarım"),
    ("pencere-ustu", "pencere üstü"),
    ("duvar-boyu", "duvar boyu"),
    ("villa-mobilyasi", "villa mobilyası"),
    ("kapili", "kapılı"),
    ("aynali", "aynalı"),
    ("aynasiz", "aynasız"),
    ("boyali", "boyalı"),
    ("cerceveli", "çerçeveli"),
    ("camli", "camlı"),
    ("citili", "çıtalı"),
    ("isikli", "ışıklı"),
    ("vitrinli", "vitrinli"),
    ("kulplu", "kulplu"),
    ("rafli", "raflı"),
    ("odasi", "odası"),
    ("dolabi", "dolabı"),
    ("dolaplari", "dolapları"),
    ("tezgahi", "tezgahı"),
    ("tezgahlari", "tezgahları"),
    ("unitesi", "ünitesi"),
    ("takimi", "takımı"),
    ("mobilyasi", "mobilyası"),
    ("kitaplik", "kitaplık"),
    ("yukluk", "yüklük"),
    ("luks", "lüks"),
    ("ust", "üst"),
    ("ustu", "üstü"),
    ("elbise", "elbise"),
    ("makyaj", "makyaj"),
    ("geometrik", "geometrik"),
    ("kiler", "kiler"),
    ("parlak", "parlak"),
    ("spot", "spot"),
    ("oval", "oval"),
    ("krem", "krem"),
    ("gold", "gold"),
    ("gri", "gri"),
    ("mavi", "mavi"),
    ("beyaz", "beyaz"),
    ("lake", "lake"),
    ("led", "LED"),
    ("pvc", "PVC"),
    ("tv", "TV"),
    ("ikili", "ikili"),
    ("imalat", "imalat"),
    ("vestiyer", "vestiyer"),
    ("mutfak", "mutfak"),
    ("gardrop", "gardırop"),
    ("villa", "villa"),
    ("l", "L"),
]

OVERRIDES = {
    "amerikan-tarzi-mutfak-dolabi": "Amerikan tarzı ada tezgahlı mutfak dolabı",
    "camli-makyaj-unitesi-gardrop": "Camlı kapaklı makyaj üniteli gardırop",
    "l-gri-camli-mutfak-dolabi": "L biçimli gri camlı mutfak dolabı",
    "l-mutfak-dolabi-pencere-ustu": "Pencere üstü L mutfak dolabı",
    "beyaz-cerceveli-vestiyer": "Beyaz çerçeveli antre vestiyeri",
    "geometrik-camli-vestiyer": "Geometrik camlı aynalı vestiyer",
    "tv-unitesi-citili-panel-villa-mobilyasi": "Çıtalı panelli TV ünitesi",
    "gri-oval-aynali-gardrop": "Gri oval aynalı çıtalı gardırop",
    "mavi-citili-gardrop": "Mavi çıtalı oval kapaklı gardırop",
}

PAGES = {
    "gardrop": {
        "file": ROOT / "urunler" / "gardrop-yatak-odasi.html",
        "anchor": '    <section class="section section-muted" id="gorseller">',
        "loc": "https://eminkapiosmaniye.com/urunler/gardrop-yatak-odasi.html",
        "eyebrow": "Uygulama",
        "title": "Montajdan gardırop kareleri",
        "lead": "Ölçüye özel gardırop işleri. Şeridi sağa sola kaydırın, görsele tıklayınca tam sayfa açılır.",
    },
    "mutfak": {
        "file": ROOT / "urunler" / "mutfak-dolabi.html",
        "anchor": '    <section class="section section-muted" id="galeri">',
        "loc": "https://eminkapiosmaniye.com/urunler/mutfak-dolabi.html",
        "eyebrow": "Uygulama",
        "title": "Montajdan mutfak kareleri",
        "lead": "Ölçüye özel mutfak dolabı işleri. Şeridi sağa sola kaydırın, görsele tıklayınca tam sayfa açılır.",
    },
    "villa": {
        "file": ROOT / "urunler" / "villa-mobilyasi.html",
        "anchor": '    <section class="section section-muted" id="gorseller">',
        "loc": "https://eminkapiosmaniye.com/urunler/villa-mobilyasi.html",
        "eyebrow": "Uygulama",
        "title": "Villa mobilyası uygulamaları",
        "lead": "Mutfak, gardırop, vestiyer ve TV ünitesi işleri. Şeridi kaydırın, görsele tıklayınca tam sayfa açılır.",
    },
    "vestiyer": {
        "file": ROOT / "urunler" / "vestiyer.html",
        "anchor": '    <section class="section section-muted" id="gorseller">',
        "loc": "https://eminkapiosmaniye.com/urunler/vestiyer.html",
        "eyebrow": "Uygulama",
        "title": "Montajdan vestiyer kareleri",
        "lead": "Antre ve vestiyer işleri. Şeridi sağa sola kaydırın, görsele tıklayınca tam sayfa açılır.",
    },
}


def caption_for(stem: str) -> str:
    if stem in OVERRIDES:
        return OVERRIDES[stem]
    parts = stem.split("-")
    out: list[str] = []
    i = 0
    while i < len(parts):
        matched = False
        for n in range(min(3, len(parts) - i), 0, -1):
            chunk = "-".join(parts[i : i + n])
            for en, tr in TR:
                if chunk == en:
                    out.append(tr)
                    i += n
                    matched = True
                    break
            if matched:
                break
        if not matched:
            out.append(parts[i])
            i += 1
    text = " ".join(out)
    text = re.sub(r"\s+", " ", text).strip()
    if text:
        text = text[0].upper() + text[1:]
    return text


def pages_for(stem: str) -> list[str]:
    found = []
    if "gardrop" in stem:
        found.append("gardrop")
    if "mutfak" in stem:
        found.append("mutfak")
    if "vestiyer" in stem:
        found.append("vestiyer")
    if "villa" in stem:
        found.append("villa")
    return found


def convert(path: Path) -> tuple[int, int]:
    im = ImageOps.exif_transpose(Image.open(path))
    im = im.convert("RGB")
    w, h = im.size
    scale = min(1.0, 1600 / max(w, h))
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    dest = OUT_DIR / f"{path.stem}.webp"
    im.save(dest, "WEBP", quality=78, method=4)
    return im.size


def figure_html(stem: str, size: tuple[int, int], lazy: bool) -> str:
    cap = caption_for(stem)
    alt = f"{cap} — Emin Kapı Osmaniye"
    src = f"{WEB_PREFIX}/{stem}.webp"
    w, h = size
    loading = ' loading="lazy"' if lazy else ""
    return (
        f"""            <figure>
              <img src="{src}" alt="{escape(alt, quote=True)}" width="{w}" height="{h}"{loading} />
              <figcaption>{escape(cap)}</figcaption>
            </figure>"""
    )


def section_html(page_key: str, items: list[tuple[str, tuple[int, int]]]) -> str:
    meta = PAGES[page_key]
    figures = "\n".join(figure_html(stem, size, i > 0) for i, (stem, size) in enumerate(items))
    return f"""<!-- uygulamalar:start -->
    <section class="section" id="uygulamalar">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">{escape(meta["eyebrow"])}</p>
          <h2>{escape(meta["title"])}</h2>
          <p>{escape(meta["lead"])}</p>
        </div>
        <div class="job-strip" data-job-strip>
          <button type="button" class="job-strip__nav job-strip__nav--prev" data-job-prev aria-label="Önceki görseller">‹</button>
          <div class="job-strip__track">
{figures}
          </div>
          <button type="button" class="job-strip__nav job-strip__nav--next" data-job-next aria-label="Sonraki görseller">›</button>
        </div>
      </div>
    </section>
<!-- uygulamalar:end -->
"""


def inject_html(page_key: str, block: str) -> None:
    meta = PAGES[page_key]
    path: Path = meta["file"]
    html = path.read_text(encoding="utf-8")
    html = html.replace("../css/styles.css?v=20260912b", "../css/styles.css?v=20261006b")
    html = html.replace("../css/styles.css?v=20261006a", "../css/styles.css?v=20261006b")
    html = html.replace("../js/main.js?v=mobilya3", "../js/main.js?v=uygulama1")
    html = html.replace("../js/main.js?v=mutfak-urun3", "../js/main.js?v=uygulama1")
    start = "<!-- uygulamalar:start -->"
    end = "<!-- uygulamalar:end -->"
    if start in html and end in html:
        html = re.sub(
            re.escape(start) + r".*?" + re.escape(end),
            block.strip("\n"),
            html,
            count=1,
            flags=re.DOTALL,
        )
    else:
        anchor = meta["anchor"]
        if anchor not in html:
            raise SystemExit(f"Anchor missing in {path.name}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    path.write_text(html, encoding="utf-8")


def sitemap_images(items: list[tuple[str, tuple[int, int]]]) -> str:
    chunks = []
    for stem, _size in items:
        cap = caption_for(stem)
        loc = f"https://eminkapiosmaniye.com/assets/img/products/mobilya/uygulamalar/{stem}.webp"
        chunks.append(
            "    <image:image>\n"
            f"      <image:loc>{escape(loc)}</image:loc>\n"
            f"      <image:title>{escape(cap)}</image:title>\n"
            "    </image:image>\n"
        )
    return "".join(chunks)


def inject_sitemap(page_key: str, items: list[tuple[str, tuple[int, int]]]) -> None:
    loc = PAGES[page_key]["loc"]
    xml = SITEMAP.read_text(encoding="utf-8")
    block_re = re.compile(
        r"(<url>\s*<loc>" + re.escape(loc) + r"</loc>.*?</url>)",
        re.DOTALL,
    )
    match = block_re.search(xml)
    if not match:
        raise SystemExit(f"Sitemap url missing: {loc}")
    block = match.group(1)
    block = re.sub(r"<lastmod>[^<]+</lastmod>", "<lastmod>2026-10-06</lastmod>", block, count=1)
    extra = sitemap_images(items)
    # Drop previously injected uygulama images in this url, then append fresh ones.
    block = re.sub(
        r"\s*<image:image>\s*<image:loc>https://eminkapiosmaniye.com/assets/img/products/mobilya/uygulamalar/[^<]+</image:loc>\s*<image:title>[^<]*</image:title>\s*</image:image>",
        "",
        block,
    )
    block = block.replace("</url>", extra + "  </url>")
    xml = xml[: match.start()] + block + xml[match.end() :]
    SITEMAP.write_text(xml, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[tuple[str, tuple[int, int]]]] = {k: [] for k in PAGES}
    files = sorted(
        p
        for p in SRC.iterdir()
        if p.is_file() and p.suffix.lower() in {".jfif", ".jpg", ".jpeg", ".png", ".webp"}
    )
    used = 0
    for path in files:
        if path.stem in SKIP:
            print(f"skip {path.name}")
            continue
        targets = pages_for(path.stem)
        if not targets:
            raise SystemExit(f"No page for {path.name}")
        size = convert(path)
        used += 1
        print(f"{path.name} -> {path.stem}.webp {size} => {', '.join(targets)}")
        for key in targets:
            grouped[key].append((path.stem, size))

    order = {"mutfak": 0, "gardrop": 1, "vestiyer": 2, "tv": 3}

    def sort_key(item: tuple[str, tuple[int, int]]) -> tuple[int, str]:
        stem = item[0]
        if "mutfak" in stem:
            bucket = 0
        elif "gardrop" in stem:
            bucket = 1
        elif "vestiyer" in stem:
            bucket = 2
        else:
            bucket = 3
        return (bucket, stem)

    for key, items in grouped.items():
        items.sort(key=sort_key)
        print(f"{key}: {len(items)}")
        inject_html(key, section_html(key, items))
        inject_sitemap(key, items)
    print(f"converted {used}")


if __name__ == "__main__":
    main()
