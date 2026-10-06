# -*- coding: utf-8 -*-
"""Copy ciftkanatli job photos into the site as two WebP sizes. Does not touch originals."""
from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image, ImageOps

SRC = Path(r"C:\Users\mosta\Desktop\Eminkapi_doneler\ciftkanatli")
OUT = Path(r"C:\Users\mosta\Desktop\emin-kapi-full\assets\img\rehber\cift-kanatli")
MANIFEST = OUT / "esleme.json"

TR = str.maketrans(
    {
        "ç": "c",
        "Ç": "c",
        "ğ": "g",
        "Ğ": "g",
        "ı": "i",
        "İ": "i",
        "I": "i",
        "ö": "o",
        "Ö": "o",
        "ş": "s",
        "Ş": "s",
        "ü": "u",
        "Ü": "u",
    }
)


def slugify(stem: str) -> str:
    s = stem.translate(TR).lower()
    s = s.replace("apartaman", "apartman")
    s = s.replace("apartan", "apartman")
    s = s.replace("thermo-woord", "thermo-wood")
    s = s.replace("_", "-").replace(" ", "-")
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    s = re.sub(r"([a-z])(\d+)$", r"\1-\2", s)
    return s


def pages_for(slug: str) -> list[str]:
    tokens = set(slug.split("-"))
    found: list[str] = []

    def add(page: str) -> None:
        if page not in found:
            found.append(page)

    if "cift-kanat" in slug:
        add("bina-giris-kapisi")
        add("apartman-kapisi")
        add("villa-giris-kapisi")
    glass = {
        t
        for t in tokens
        if t in {"cam", "camli", "ayna", "aynali", "aynacamli"}
        or (("ayna" in t or t.startswith("cam")) and t != "camsiz" and not t.startswith("camsiz"))
    }
    if glass:
        add("camli-bina-kapisi")
    if "beyaz" in tokens:
        add("beyaz-renkli-kapi")
    if "villa" in tokens:
        add("villa-giris-kapisi")
    if "apartman" in tokens:
        add("apartman-kapisi")
    if "bina" in tokens or "giris" in tokens:
        add("bina-giris-kapisi")
    if "pencreli" in tokens or "pencere" in tokens or "pencereli" in tokens:
        add("camli-bina-kapisi")
    if "kompozit" in tokens:
        add("bina-giris-kapisi")
    if "cift-acilir" in slug:
        add("bina-giris-kapisi")
    if "thermo-wood" in slug or "thermowood" in slug:
        add("villa-giris-kapisi")
    if slug in {
        "komple-metal-dort-mevsim-yavru-kanatli-celik-kapi",
        "laminoks-yavru-kanatli-antrasit-siyah-kapi",
    }:
        add("bina-giris-kapisi")
    if slug.startswith("luks-laminoks-kapi-modeli") or slug.startswith(
        "luks-pvc-kabartma-celik-kapi-modeli"
    ):
        add("osmaniye-celik-kapi-fiyatlari")
    add("osmaniye-celik-kapi-fiyatlari")
    return found


def save_limited(im: Image.Image, dest: Path, max_bytes: int) -> tuple[int, int]:
    quality = 80
    size = max_bytes + 1
    while quality >= 30:
        im.save(dest, "WEBP", quality=quality, method=6)
        size = dest.stat().st_size
        if size <= max_bytes:
            return quality, size
        quality -= 5
    return quality + 5, size


def resized(im: Image.Image, max_edge: int) -> Image.Image:
    w, h = im.size
    long_edge = max(w, h)
    if long_edge <= max_edge:
        return im
    scale = max_edge / long_edge
    return im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(
        (p for p in SRC.iterdir() if p.is_file() and p.suffix.lower() in {".jfif", ".jpg", ".jpeg", ".png", ".webp"}),
        key=lambda p: p.name.casefold(),
    )
    used: dict[str, int] = {}
    rows = []
    for src in files:
        slug = slugify(src.stem)
        n = used.get(slug, 0) + 1
        used[slug] = n
        if n > 1:
            slug = f"{slug}-{n}"
        with Image.open(src) as raw:
            im = ImageOps.exif_transpose(raw)
            im = im.convert("RGB")
            native = im.size
        large = resized(im, 1600)
        small = resized(im, 800)
        large_name = f"{slug}-1600.webp"
        small_name = f"{slug}-800.webp"
        q_large, b_large = save_limited(large, OUT / large_name, 200 * 1024)
        q_small, b_small = save_limited(small, OUT / small_name, 100 * 1024)
        rows.append(
            {
                "original": src.name,
                "slug": slug,
                "pages": pages_for(slug),
                "native": [native[0], native[1]],
                "original_bytes": src.stat().st_size,
                "large": large_name,
                "large_px": [large.size[0], large.size[1]],
                "large_bytes": b_large,
                "large_q": q_large,
                "small": small_name,
                "small_px": [small.size[0], small.size[1]],
                "small_bytes": b_small,
                "small_q": q_small,
            }
        )
        print(f"{src.name} -> {slug} {rows[-1]['pages'] or '-'} {b_large}/{b_small}")

    MANIFEST.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    over_large = [r for r in rows if r["large_bytes"] > 200 * 1024]
    over_small = [r for r in rows if r["small_bytes"] > 100 * 1024]
    print(f"count {len(rows)} over200 {len(over_large)} over100 {len(over_small)}")


if __name__ == "__main__":
    main()
