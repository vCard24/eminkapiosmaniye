# -*- coding: utf-8 -*-
"""Convert camli modeller images and inject catalog gallery into camli-ic-kapi.html."""
from __future__ import annotations

import os
import re
from html import escape
from pathlib import Path

from PIL import Image

SRC = Path(r"C:\Users\mosta\Desktop\maria-DB\eminkapiosmaniye-camlimodeller")
OUT_DIR = Path(r"c:\Users\mosta\Desktop\emin-kapi-full\assets\img\products\camli\modeller")
HTML_PATH = Path(r"c:\Users\mosta\Desktop\emin-kapi-full\urunler\camli-ic-kapi.html")
WEB_PREFIX = "../assets/img/products/camli/modeller"

# Longer phrases first
TR_WORDS = [
    ("yikanabilir", "yıkanabilir"),
    ("pencereleli", "pencereli"),
    ("kanatli", "kanatlı"),
    ("pervazli", "pervazlı"),
    ("panelli", "panelli"),
    ("kasali", "kasalı"),
    ("boyali", "boyalı"),
    ("renkli", "renkli"),
    ("camli", "camlı"),
    ("camsiz", "camsız"),
    ("seffaf", "şeffaf"),
    ("cicek", "çiçek"),
    ("cift", "çift"),
    ("acilir", "açılır"),
    ("buyuk", "büyük"),
    ("genis", "geniş"),
    ("gobekli", "göbekli"),
    ("cerceveli", "çerçeveli"),
    ("ustten", "üstten"),
    ("saga", "sağa"),
    ("dort", "dört"),
    ("luks", "lüks"),
    ("icin", "için"),
    ("ornegi", "örneği"),
    ("odalar", "odalar"),
    ("odasi", "odası"),
    ("kapilari", "kapıları"),
    ("kapisi", "kapısı"),
    ("dairesi", "dairesi"),
    ("girisi", "girişi"),
    ("acik", "açık"),
    ("hali", "hali"),
    ("desenli", "desenli"),
    ("kayarak", "kayarak"),
    ("kayan", "kayan"),
    ("kayar", "kayar"),
    ("ikili", "ikili"),
    ("yan", "yan"),
    ("yana", "yana"),
    ("tam", "tam"),
    ("yarim", "yarım"),
    ("buzlu", "buzlu"),
    ("siyah", "siyah"),
    ("beyaz", "beyaz"),
    ("antrasit", "antrasit"),
    ("krem", "krem"),
    ("bej", "bej"),
    ("gri", "gri"),
    ("gold", "gold"),
    ("lake", "lake"),
    ("lakeli", "lakeli"),
    ("kompozit", "kompozit"),
    ("panel", "panel"),
    ("pervaz", "pervaz"),
    ("mutfak", "mutfak"),
    ("banyo", "banyo"),
    ("tuvalet", "tuvalet"),
    ("misafir", "misafir"),
    ("daire", "daire"),
    ("villa", "villa"),
    ("apartman", "apartman"),
    ("pvc", "PVC"),
    ("membran", "membran"),
    ("modeli", "modeli"),
    ("modelleri", "modelleri"),
    ("model", "model"),
    ("uygulama", "uygulama"),
    ("deseni", "deseni"),
    ("cizgili", "çizgili"),
    ("yavru", "yavru"),
    ("tek", "tek"),
    ("iki", "iki"),
    ("ve", "ve"),
    ("ile", "ile"),
    ("icin", "için"),
    ("ic", "iç"),
    ("oda", "oda"),
    ("ev", "ev"),
    ("kapi", "kapı"),
    ("kar", "kar"),
    ("buz", "buz"),
]


def stem_to_caption(stem: str) -> str:
    s = stem.lower().replace("_", "-")
    # Apply multi-word replacements on hyphen tokens
    parts = s.split("-")
    out = []
    i = 0
    while i < len(parts):
        matched = False
        for n in range(min(3, len(parts) - i), 0, -1):
            chunk = "-".join(parts[i : i + n])
            for en, tr in TR_WORDS:
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


def convert_images() -> list[tuple[str, str]]:
    """Returns list of (webp_filename, caption)."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # clear previous modeller webps we own (keep parent camli assets)
    for old in OUT_DIR.glob("*.webp"):
        old.unlink()

    items: list[tuple[str, str]] = []
    files = sorted(
        f
        for f in SRC.iterdir()
        if f.is_file() and f.suffix.lower() in {".jfif", ".jpg", ".jpeg", ".png", ".webp"}
    )
    for f in files:
        caption = stem_to_caption(f.stem)
        out_name = f.stem + ".webp"
        out_path = OUT_DIR / out_name
        im = Image.open(f)
        im = im.convert("RGB")
        # Limit long edge for web
        max_edge = 1400
        w, h = im.size
        scale = min(1.0, max_edge / max(w, h))
        if scale < 1:
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        im.save(out_path, "WEBP", quality=82, method=4)
        items.append((out_name, caption))
        print(f"  {f.name} -> {out_name}")
    return items


def build_thumbs_html(items: list[tuple[str, str]]) -> str:
    blocks = []
    total = len(items)
    for idx, (fname, caption) in enumerate(items):
        src = f"{WEB_PREFIX}/{fname}"
        code = caption
        label = "Camlı iç kapı"
        active = " is-active" if idx == 0 else ""
        lazy = "" if idx == 0 else ' loading="lazy"'
        blocks.append(
            f"""              <button type="button" class="catalog__thumb{active}" role="listitem" data-catalog-thumb data-code="{escape(code, quote=True)}" data-label="{escape(label, quote=True)}" data-src="{src}" aria-label="{escape(code, quote=True)}">
                <img src="{src}" alt="{escape(code, quote=True)}" width="200" height="280"{lazy} />
                <span class="catalog__thumb-code">{escape(code)}</span>
              </button>"""
        )
    return "\n".join(blocks)


def build_catalog_section(items: list[tuple[str, str]]) -> str:
    first_src = f"{WEB_PREFIX}/{items[0][0]}"
    first_cap = items[0][1]
    total = len(items)
    thumbs = build_thumbs_html(items)
    return f"""    <section class="catalog catalog--camli" data-catalog aria-label="Camlı iç kapı model kataloğu">
      <div class="wrap">
        <div class="catalog__layout">
          <div class="catalog__stage">
            <button type="button" class="catalog__stage-img" data-catalog-zoom aria-label="Büyüt">
              <img data-catalog-stage src="{first_src}" alt="{escape(first_cap, quote=True)} — Emin Kapı Osmaniye" width="600" height="900" />
            </button>
            <div class="catalog__stage-meta">
              <div>
                <strong data-catalog-code>{escape(first_cap)}</strong>
                <span data-catalog-label>Camlı iç kapı</span>
              </div>
              <div style="display:flex;align-items:center;gap:.75rem">
                <span data-catalog-count><b>01</b> / {total:02d}</span>
                <div class="catalog__nav-btns">
                  <button type="button" data-catalog-prev aria-label="Önceki">‹</button>
                  <button type="button" data-catalog-next aria-label="Sonraki">›</button>
                </div>
              </div>
            </div>
          </div>

          <aside class="catalog__side">
            <div class="catalog__side-head">
              <p class="eyebrow">Modeller</p>
              <h2>Hızlı seçim</h2>
              <p>Bir modele dokunun — solda / üstte büyür. Tam ekranda oklar veya kaydırma ile gezin.</p>
            </div>
            <div class="catalog__thumbs" role="list">
{thumbs}
            </div>
            <p style="margin:0;color:rgba(255,255,255,.45);font-size:.85rem">Fiyat: ölçü, renk, cam ve modele göre — keşif sonrası teklif.</p>
            <p style="display:flex;flex-wrap:wrap;gap:.6rem;margin:0">
              <a class="btn btn-gold" href="tel:+905422362365">0542 236 236 5</a>
              <a class="btn btn-ghost" href="../iletisim.html">İletişim</a>
            </p>
          </aside>
        </div>
      </div>
    </section>
"""


MARKER_START = "<!-- camli-catalog:start -->"
MARKER_END = "<!-- camli-catalog:end -->"


def inject_html(section: str) -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    block = f"{MARKER_START}\n{section}{MARKER_END}"

    if MARKER_START in html and MARKER_END in html:
        html = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            block,
            html,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Insert right after page-hero section closes
        needle = '    </section>\n    <section class="section" id="ornekler">'
        if needle not in html:
            raise SystemExit("Could not find insertion point after page-hero")
        html = html.replace(
            needle,
            f"    </section>\n\n{block}\n    <section class=\"section\" id=\"ornekler\">",
            1,
        )

    HTML_PATH.write_text(html, encoding="utf-8")


def main() -> None:
    print("Converting images…")
    items = convert_images()
    print(f"Converted {len(items)} images")
    print("Building catalog HTML…")
    section = build_catalog_section(items)
    inject_html(section)
    print(f"Injected catalog into {HTML_PATH}")
    # sample captions
    print("Sample captions:")
    for _, c in items[:5]:
        print(f"  - {c}")


if __name__ == "__main__":
    main()
