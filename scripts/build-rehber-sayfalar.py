# -*- coding: utf-8 -*-
"""Build the five guide articles from EK B. Does not edit the article source."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "cursor-prompt-emin-kapi-rehber.md"
MANIFEST = ROOT / "assets" / "img" / "rehber" / "cift-kanatli" / "esleme.json"
TEMPLATE = ROOT / "rehber" / "osmaniye-celik-kapi-fiyatlari.html"
IMG = "../assets/img/rehber/cift-kanatli"
SITE = "https://eminkapiosmaniye.com"
DATE = "2026-10-06"

LINKS = {
    "https://eminkapiosmaniye.com/osmaniye-celik-kapi-fiyatlari/": "osmaniye-celik-kapi-fiyatlari.html",
    "https://eminkapiosmaniye.com/osmaniye-celik-kapi/": "../urunler/celik-kapi.html",
    "https://eminkapiosmaniye.com/osmaniye-kapi-modelleri/": "../urunler/index.html",
    "https://eminkapiosmaniye.com/oda-kapi-modelleri/": "../urunler/ic-oda-kapisi.html",
    "https://eminkapiosmaniye.com/luks-ic-kapi-modelleri/": "../urunler/luks-ic-kapi.html",
}

PAGES = [
    {
        "file": "bina-giris-kapisi.html",
        "key": "bina-giris-kapisi",
        "n": 1,
        "focus": "Bina Giriş Kapısı",
        "short": "Bina Giriş Kapısı",
        "title": "Bina Giriş Kapısı: 7 Önemli Seçim Kriteri | Osmaniye",
        "description": "Bina giriş kapısı modelleri, malzeme seçenekleri ve fiyatı etkileyen unsurlar. Osmaniye'de üretici Emin Kapı'dan ölçüye özel üretim ve montaj için arayın.",
        "featured_alt": "Bina giriş kapısı modeli – Emin Kapı Osmaniye",
        "featured": "lazerli-bina-giris-kapisi",
    },
    {
        "file": "apartman-kapisi.html",
        "key": "apartman-kapisi",
        "n": 2,
        "focus": "Apartman Kapısı",
        "short": "Apartman Kapısı",
        "title": "Apartman Kapısı Modelleri ve 5 Kritik Seçim İpucu | Osmaniye",
        "description": "Apartman kapısı seçerken güvenlik, malzeme ve kilit sistemine dikkat edin. Osmaniye ve ilçelerinde Emin Kapı'dan ölçüye özel apartman kapısı üretimi.",
        "featured_alt": "Apartman kapısı modeli – Emin Kapı Osmaniye",
        "featured": "luks-apartman-giris-kapisi",
    },
    {
        "file": "villa-giris-kapisi.html",
        "key": "villa-giris-kapisi",
        "n": 3,
        "focus": "Villa Giriş Kapısı",
        "short": "Villa Giriş Kapısı",
        "title": "Villa Giriş Kapısı: 6 Şık ve Güvenli Model | Osmaniye",
        "description": "Villa giriş kapısı modelleri: pivot, çift kanat ve dış iklim serisi. Osmaniye'de üretici Emin Kapı ile villanıza özel ölçü, renk ve kaplama seçenekleri.",
        "featured_alt": "Villa giriş kapısı modeli – Emin Kapı Osmaniye",
        "featured": "thermo-wood-izolasyonlu-kapi",
    },
    {
        "file": "beyaz-renkli-kapi.html",
        "key": "beyaz-renkli-kapi",
        "n": 4,
        "focus": "Beyaz Renkli Kapı",
        "short": "Beyaz Renkli Kapı",
        "title": "Beyaz Renkli Kapı: 5 Zamansız Dekorasyon Fikri | Emin Kapı",
        "description": "Beyaz renkli kapı modelleri evinizi ferah ve modern gösterir. Lake, PVC ve çelik seçenekleriyle Osmaniye Emin Kapı'dan beyaz renkli kapı çözümleri.",
        "featured_alt": "Beyaz renkli kapı modeli – Emin Kapı Osmaniye",
        "featured": "beyaz-kapi-modeli-selcuklu-motifi",
    },
    {
        "file": "camli-bina-kapisi.html",
        "key": "camli-bina-kapisi",
        "n": 5,
        "focus": "Camlı Bina Kapısı",
        "short": "Camlı Bina Kapısı",
        "title": "Camlı Bina Kapısı: 6 Güvenli ve Modern Seçenek | Osmaniye",
        "description": "Camlı bina kapısı ile apartman girişiniz aydınlık ve güvenli olsun. Temperli ve lamine camlı modeller Osmaniye Emin Kapı'da; keşif için hemen arayın.",
        "featured_alt": "Camlı bina kapısı modeli – Emin Kapı Osmaniye",
        "featured": "lazer-kesim-camli-bina-giris-kapisi",
    },
]

WORD = {
    "acilir": "açılır",
    "acilmaz": "açılmaz",
    "agac": "ağaç",
    "antrasit": "antrasit",
    "apartman": "apartman",
    "ayna": "ayna",
    "aynali": "aynalı",
    "aynacamli": "ayna camlı",
    "beyaz": "beyaz",
    "bina": "bina",
    "bir": "bir",
    "buyuk": "büyük",
    "camli": "camlı",
    "camsiz": "camsız",
    "celik": "çelik",
    "cift": "çift",
    "daire": "daire",
    "dort": "dört",
    "duvara": "duvara",
    "giris": "giriş",
    "gorunum": "görünüm",
    "icten": "içten",
    "iki": "iki",
    "is": "iş",
    "isiklikli": "ışıklı",
    "kabartma": "kabartma",
    "kabartmali": "kabartmalı",
    "kahverengi": "kahverengi",
    "kanat": "kanat",
    "kanatli": "kanatlı",
    "kapi": "kapı",
    "kapisi": "kapısı",
    "kasali": "kasalı",
    "kesim": "kesim",
    "kollu": "kollu",
    "kompozit": "kompozit",
    "lambiri": "lambiri",
    "laminoks": "laminoks",
    "lazer": "lazer",
    "lazerli": "lazerli",
    "luks": "lüks",
    "metal": "metal",
    "mevsim": "mevsim",
    "modeli": "modeli",
    "montajli": "montajlı",
    "motifi": "motifi",
    "motifli": "motifli",
    "orta": "orta",
    "ozel": "özel",
    "panel": "panel",
    "pencreli": "pencereli",
    "pvc": "PVC",
    "sabit": "sabit",
    "sac": "sac",
    "selcuklu": "Selçuklu",
    "siyah": "siyah",
    "sol": "sol",
    "tam": "tam",
    "tan": "tan",
    "tarafi": "tarafı",
    "tek": "tek",
    "thermo": "thermo",
    "uc": "üç",
    "ustten": "üstten",
    "ve": "ve",
    "wood": "wood",
    "yan": "yan",
    "yanyana": "yan yana",
    "yapilmis": "yapılmış",
    "yavru": "yavru",
    "yeri": "yeri",
}


def slug_id(text: str) -> str:
    s = text.replace("İ", "i").replace("I", "i")
    s = s.translate(str.maketrans({
        "ç": "c", "Ç": "c", "ğ": "g", "Ğ": "g", "ı": "i", "ö": "o", "Ö": "o",
        "ş": "s", "Ş": "s", "ü": "u", "Ü": "u",
    })).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "bolum"


def attr(text: str) -> str:
    return html.escape(text, quote=False).replace('"', "&quot;")


def inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    def repl_link(match: re.Match[str]) -> str:
        label = match.group(1)
        href = html.unescape(match.group(2))
        href = LINKS.get(href, href)
        extra = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return f'<a href="{html.escape(href, quote=True)}"{extra}>{label}</a>'
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_link, escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = escaped.replace(
        "<strong>0542 236 236 5</strong>",
        '<strong><a href="tel:+905422362365">0542 236 236 5</a></strong>',
    )
    return escaped


def parse_article(raw: str) -> tuple[str, str, list[tuple[str, str]]]:
    lines = raw.strip().splitlines()
    if not lines or not lines[0].startswith("# "):
        raise SystemExit("article missing h1")
    h1 = lines[0][2:].strip()
    body = lines[1:]
    html_parts: list[str] = []
    faqs: list[tuple[str, str]] = []
    ids: dict[str, int] = {}
    i = 0
    in_faq = False
    while i < len(body):
        line = body[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            in_faq = title == "Sıkça Sorulan Sorular"
            hid = unique_id(slug_id(title), ids)
            html_parts.append(f'<h2 id="{hid}">{inline(title)}</h2>')
            i += 1
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            hid = unique_id(slug_id(title), ids)
            html_parts.append(f'<h3 id="{hid}">{inline(title)}</h3>')
            i += 1
            if in_faq:
                while i < len(body) and not body[i].strip():
                    i += 1
                answer_lines: list[str] = []
                while i < len(body) and body[i].strip() and not body[i].startswith("#"):
                    answer_lines.append(body[i].strip())
                    i += 1
                answer = " ".join(answer_lines)
                faqs.append((title, answer))
                if answer:
                    html_parts.append(f"<p>{inline(answer)}</p>")
            continue
        if line.startswith("|"):
            rows: list[str] = []
            while i < len(body) and body[i].startswith("|"):
                rows.append(body[i])
                i += 1
            html_parts.append(table_html(rows))
            continue
        if re.match(r"^\d+\. ", line):
            items: list[str] = []
            while i < len(body) and re.match(r"^\d+\. ", body[i]):
                items.append(re.sub(r"^\d+\. ", "", body[i]))
                i += 1
            lis = "".join(f"<li>{inline(item)}</li>" for item in items)
            html_parts.append(f"<ol>{lis}</ol>")
            continue
        if line.startswith("- "):
            items = []
            while i < len(body) and body[i].startswith("- "):
                items.append(body[i][2:])
                i += 1
            lis = "".join(f"<li>{inline(item)}</li>" for item in items)
            html_parts.append(f"<ul>{lis}</ul>")
            continue
        para = [line.strip()]
        i += 1
        while i < len(body) and body[i].strip() and not body[i].startswith(("#", "|", "- ")) and not re.match(r"^\d+\. ", body[i]):
            para.append(body[i].strip())
            i += 1
        html_parts.append(f"<p>{inline(' '.join(para))}</p>")
    if not html_parts or not html_parts[0].startswith("<p>"):
        raise SystemExit("intro paragraph missing")
    return h1, "\n".join(html_parts), faqs


def unique_id(base: str, ids: dict[str, int]) -> str:
    n = ids.get(base, 0) + 1
    ids[base] = n
    return base if n == 1 else f"{base}-{n}"


def table_html(rows: list[str]) -> str:
    parsed = []
    for row in rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        parsed.append(cells)
    if not parsed:
        return ""
    head = "".join(f"<th scope=\"col\">{inline(cell)}</th>" for cell in parsed[0])
    body = []
    for cells in parsed[1:]:
        tds = "".join(f"<td>{inline(cell)}</td>" for cell in cells)
        body.append(f"<tr>{tds}</tr>")
    return (
        '<div class="spec-scroll"><table class="spec-table"><thead><tr>'
        + head
        + "</tr></thead><tbody>"
        + "".join(body)
        + "</tbody></table></div>"
    )


def human_alt(slug: str, focus: str) -> str:
    words = [WORD.get(part, part) for part in slug.split("-")]
    phrase = " ".join(words)
    phrase = phrase[:1].upper() + phrase[1:]
    return f"{phrase} — {focus}"


def figure(row: dict, alt: str, featured: bool = False) -> str:
    w, h = row["large_px"]
    large = f"{IMG}/{row['large']}"
    small = f"{IMG}/{row['small']}"
    loading = 'loading="eager" fetchpriority="high"' if featured else 'loading="lazy"'
    sizes = "(max-width: 560px) 90vw, 420px" if featured else "(max-width: 560px) 45vw, 18vw"
    return (
        "<figure>"
        f'<img src="{large}" srcset="{small} 800w, {large} 1600w" sizes="{sizes}" '
        f'alt="{html.escape(alt, quote=True)}" width="{w}" height="{h}" {loading} />'
        "</figure>"
    )


def chrome_blocks() -> tuple[str, str, str]:
    text = TEMPLATE.read_text(encoding="utf-8")
    blocks = []
    for name in ("topbar", "header", "footer"):
        start = f"<!-- chrome:{name}:start -->"
        end = f"<!-- chrome:{name}:end -->"
        a = text.index(start)
        b = text.index(end) + len(end)
        block = text[a:b].replace(' aria-current="page"', "")
        blocks.append(block)
    return blocks[0], blocks[1], blocks[2]


def toc_html(article_html: str) -> str:
    titles = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', article_html)
    items = "".join(f'<li><a href="#{hid}">{title}</a></li>' for hid, title in titles)
    return f'<nav aria-label="İçindekiler"><p class="eyebrow">İçindekiler</p><ol>{items}</ol></nav>'


def related_html(current: str) -> str:
    items = []
    for page in PAGES:
        if page["file"] == current:
            continue
        items.append(f'<li><a href="{page["file"]}">{page["short"]}</a></li>')
    items.append('<li><a href="osmaniye-celik-kapi-fiyatlari.html">Çelik kapı fiyatları</a></li>')
    return (
        '<section class="section" id="ilgili-rehberler">'
        '<div class="wrap">'
        '<div class="section-head reveal"><p class="eyebrow">Rehber</p><h2>İlgili rehberler</h2></div>'
        f'<ul class="rehber-related reveal">{"".join(items)}</ul>'
        "</div></section>"
    )


def schema(page: dict, h1: str, faqs: list[tuple[str, str]], image_url: str) -> str:
    url = f"{SITE}/rehber/{page['file']}"
    graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Anasayfa", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Bilgi / Fiyat Rehberi", "item": f"{SITE}/rehber/"},
                {"@type": "ListItem", "position": 3, "name": page["short"], "item": url},
            ],
        },
        {
            "@type": "Article",
            "headline": h1,
            "description": page["description"],
            "image": image_url,
            "datePublished": DATE,
            "dateModified": DATE,
            "inLanguage": "tr-TR",
            "mainEntityOfPage": url,
            "author": {"@type": "Organization", "name": "Emin Kapı"},
            "publisher": {"@type": "Organization", "name": "Emin Kapı", "url": f"{SITE}/"},
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {"@type": "Answer", "text": answer},
                }
                for question, answer in faqs
            ],
        },
    ]
    payload = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def load_articles() -> dict[int, str]:
    text = PROMPT.read_text(encoding="utf-8")
    found = {}
    for n in range(1, 6):
        start = text.index(f"<!-- MAKALE {n} BAŞLANGIÇ")
        start = text.index("\n", start) + 1
        end = text.index(f"<!-- MAKALE {n} BİTİŞ -->")
        found[n] = text[start:end].strip()
    return found


def main() -> None:
    articles = load_articles()
    rows = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_slug = {row["slug"]: row for row in rows}
    topbar, header, footer = chrome_blocks()
    for page in PAGES:
        h1, article_html, faqs = parse_article(articles[page["n"]])
        if len(faqs) != 3 or any(not answer.strip() for _, answer in faqs):
            raise SystemExit(f"faq incomplete on {page['file']}")
        intro, rest = article_html.split("</p>", 1)
        intro = intro + "</p>"
        faq_id = slug_id("Sıkça Sorulan Sorular")
        marker = f'<h2 id="{faq_id}">'
        if marker not in rest:
            raise SystemExit(f"faq missing on {page['file']}")
        middle, faq_html = rest.split(marker, 1)
        faq_html = marker + faq_html
        assigned = [row for row in rows if page["key"] in row["pages"]]
        featured_row = by_slug.get(page["featured"])
        if featured_row is None or page["key"] not in featured_row["pages"]:
            raise SystemExit(f"featured missing for {page['file']}")
        others = [row for row in assigned if row["slug"] != featured_row["slug"]]
        alts = [human_alt(row["slug"], page["focus"]) for row in others]
        if len(alts) != len(set(alts)):
            raise SystemExit(f"duplicate alts on {page['file']}")
        if page["featured_alt"] in alts:
            raise SystemExit(f"featured alt collides on {page['file']}")
        image_url = f"{SITE}/assets/img/rehber/cift-kanatli/{featured_row['large']}"
        gallery = "\n".join(figure(row, alt) for row, alt in zip(others, alts))
        url = f"{SITE}/rehber/{page['file']}"
        doc = f"""<!DOCTYPE html>
<html lang="tr" data-root="../">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(page["title"])}</title>
  <meta name="description" content="{attr(page["description"])}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="geo.region" content="TR-80" />
  <meta name="geo.placename" content="Osmaniye" />
  <link rel="canonical" href="{url}" />
  <meta property="og:locale" content="tr_TR" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Emin Kapı Osmaniye" />
  <meta property="og:title" content="{attr(page["title"])}" />
  <meta property="og:description" content="{attr(page["description"])}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{image_url}" />
  <meta property="og:image:alt" content="{attr(page["featured_alt"])}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{attr(page["title"])}" />
  <meta name="twitter:description" content="{attr(page["description"])}" />
  <meta name="twitter:image" content="{image_url}" />
  <link rel="icon" href="../assets/img/logo.png" />
  <link rel="stylesheet" href="../css/styles.css?v=20261006c" />
  <script type="application/ld+json">
  {schema(page, h1, faqs, image_url)}
  </script>
</head>
<body>
  {topbar}

  {header}

  <main>
    <section class="page-hero">
      <div class="wrap reveal">
        <nav class="breadcrumb" aria-label="Sayfa yolu">
          <a href="../index.html">Anasayfa</a><span aria-hidden="true">/</span>
          <a href="index.html">Bilgi / Fiyat Rehberi</a><span aria-hidden="true">/</span>
          <span>{html.escape(page["short"])}</span>
        </nav>
        <h1>{html.escape(h1)}</h1>
      </div>
    </section>

    <section class="section">
      <div class="wrap prose rehber-article reveal">
        {intro}
        <div class="gallery rehber-gallery rehber-feature">
          {figure(featured_row, page["featured_alt"], featured=True)}
        </div>
        {toc_html(article_html)}
        {middle}
      </div>
    </section>

    <section class="section section-muted" id="gorseller" aria-label="{attr(page["focus"])} görselleri">
      <div class="wrap">
        <div class="gallery rehber-gallery">
          {gallery}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap prose rehber-article reveal">
        {faq_html}
      </div>
    </section>

    {related_html(page["file"])}
  </main>

  {footer}
  <script src="../js/main.js?v=rehber-celik1"></script>
</body>
</html>
"""
        dest = ROOT / "rehber" / page["file"]
        dest.write_text(doc, encoding="utf-8", newline="\n")
        print(
            page["file"],
            "title", len(page["title"]),
            "desc", len(page["description"]),
            "images", 1 + len(others),
            "faq", len(faqs),
            "h1", h1,
        )


if __name__ == "__main__":
    main()
