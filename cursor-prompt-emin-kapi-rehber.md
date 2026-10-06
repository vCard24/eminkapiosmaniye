# CURSOR GÖREVİ — Emin Kapı: 5 yeni rehber sayfası + görseller + site entegrasyonu

Bu dosya görevin tamamını içerir: kurallar, aşamalar, sayfa SEO alanları ve 5 makalenin tam metni. Başka kaynağa ihtiyaç yoktur.

- **Site:** eminkapiosmaniye.com — statik HTML site (WordPress / Rank Math eklentisi YOK; Rank Math alanlarının karşılığı doğrudan HTML'e yazılacak).
- **Firma:** Emin Kapı, Osmaniye'de iç oda kapısı, dış kapı ve çelik kapı üreticisi; mobilya da yapıyor. Osmaniye'nin tüm ilçelerine, komşu ilçe ve illere hizmet vermeye çalışan, büyüyen yerel bir firma.
- **Görsel kaynağı:** `C:\Users\mosta\Desktop\Eminkapi_doneler\ciftkanatli`
- **Şablon sayfa:** `/rehber/osmaniye-celik-kapi-fiyatlari.html`
- **Hedef:** 5 makaleyi "Bilgi / Fiyat Rehberi" bölümünün altına yeni sayfalar olarak eklemek, görselleri hazırlayıp yerleştirmek, yeni sayfaları sitenin her ilgili yerine (menü, footer, sitemap, robots vb.) işlemek.

---

## DURUM — 6 Ekim 2026

Aşama 3 onaylandı. Menü, footer ve rehber listesi beş sayfayı tanıyor. `sitemap.xml` repoda yok. Mobilya uygulama şeridi (`ekim` klasörü) bu rehber görevinin parçası değildir.

| Aşama | Durum | Karar |
|---|---|---|
| 0 Keşif | Kayıtlı. | Notlar aşağıdaki bölümde. |
| 1 Görseller | Üretildi. Rapor verildi. Onay bekleniyor. | 129 kaynak, 258 WebP. HTML yok. |
| 2 Beş sayfa | Yazıldı. Rapor verildi. Onay bekleniyor. | HTML hazır. Menü, footer ve site haritası henüz yok. |
| 3 Siteye bağlama | Yazıldı. Rapor verildi. Onay bekleniyor. | Menü, footer, rehber listesi ve görsel site haritası güncellendi. `sitemap.xml` repoda yok. |
| 4 Kontrol | Yapıldı. | Kırık bağlantı ve eksik görsel yok. Apartman başlığı 60 karakter; EK A aynen bırakıldı. |

### Aşama 1 raporu

Kaynak klasör `C:\Users\mosta\Desktop\Eminkapi_doneler\ciftkanatli` okundu, değiştirilmedi. Kopyalar: `assets/img/rehber/cift-kanatli/`. Tam eşleme: `esleme.json`.

- 129 görsel. Her birinden `-1600.webp` ve `-800.webp`. Uzun kenar sınırı aşılmadı, kırpma yok, EXIF yok.
- Sınır aşımı: büyük sürümde 200 KB üstü 0, küçük sürümde 100 KB üstü 0.
- Boyut: kaynak toplam 15,9 MB → büyük sürümler 8,6 MB, küçük sürümler 3,4 MB.
- Beş sayfaya dağılım (bir görsel birden fazla sayfada sayılır): bina giriş 41, apartman 10, villa giriş 5, camlı bina 22, beyaz 3.
- 129 görselin tamamı `rehber/osmaniye-celik-kapi-fiyatlari.html` galerisine yazıldı. Bunların 71'i yalnız bu sayfada: 47 lüks laminoks, 7 lüks PVC kabartma ve 17 model (antrasit, tek kanat daire, büyük, geniş, korkuluklu bordo, üç menfezli, metal, parlak siyah, üç Selçuklu, iki siyah pervazlı, yangın çıkış, yüksek kapı). HTML henüz değişmedi; yerleri `esleme.json` içinde.
- Kopya adında düzeltilen yazımlar: `apartaman` ve `apartan` → `apartman`, `thermo-woord` → `thermo-wood`. Türkçe karakterler ASCII'ye çevrildi. Aynı ada düşen ikinci dosya `yavru-kanatli-kompozit-celik-kapi-2`.
- `camsız` geçen ve cam / ayna içermeyen tek dosya (`kompozit-tek-kanat-camsiz`) camlı sayfaya yazılmadı.
- Beyaz sayfası boş değil: `beyaz-kapi-modeli-selcuklu-motifi`, `cift-kanatli-beyaz-kapi`, `uc-kanatli-beyaz-kapi-selcuklu-motifli`.
- Ek karar (6 Ekim): `pencreli-kapi-modeli` camlı sayfada. Adında kompozit geçenler, `cift-acilir` geçenler, `komple-metal-dort-mevsim-yavru-kanatli-celik-kapi` ve `laminoks-yavru-kanatli-antrasit-siyah-kapi` bina giriş sayfasında. İki thermo wood villada. Villa 5 görsel. 129 görselin tamamı çelik kapı fiyat sayfasında.

Eşleşenler (kaynak adı → kopya kökü → sayfalar):

| Kaynak | Kopya | Sayfalar |
|---|---|---|
| antrasit-siyah-laminoks-apartan-kapisi-cift-kanatli | antrasit-siyah-laminoks-apartman-kapisi-cift-kanatli | bina, apartman, villa |
| apartaman-giris-buyuk-kapi | apartman-giris-buyuk-kapi | apartman, bina |
| apartman-giris-siyah-camli-kapi | apartman-giris-siyah-camli-kapi | camlı, apartman, bina |
| ayna-camli-laminoks-apartman-kapisi | ayna-camli-laminoks-apartman-kapisi | camlı, apartman |
| aynacamli-bina-kapisi | aynacamli-bina-kapisi | camlı, bina |
| aynali-yavru-kanatli-kompozit-bina-giris-kapisi | aynali-yavru-kanatli-kompozit-bina-giris-kapisi | camlı, bina |
| beyaz-kapi-modeli-selcuklu-motifi | beyaz-kapi-modeli-selcuklu-motifi | beyaz |
| bina-kapisi-icten-gorunum | bina-kapisi-icten-gorunum | bina |
| cift-acilir-lazer-kesim-ayna-camli-giris-kapisi | cift-acilir-lazer-kesim-ayna-camli-giris-kapisi | camlı, bina |
| cift-kanatli-beyaz-kapi | cift-kanatli-beyaz-kapi | bina, apartman, villa, beyaz |
| cift-kanatli-cift-acilir-camli-bina-giris-kapisi | cift-kanatli-cift-acilir-camli-bina-giris-kapisi | bina, apartman, villa, camlı |
| cift-sabit-orta-acilir-lazerli-bina-kapisi | cift-sabit-orta-acilir-lazerli-bina-kapisi | bina |
| iki-acilir-…-camli-kasali | iki-acilir-bir-acilir-yavru-kanat-bir-acilir-tam-kanat-sabit-acilmaz-camli-kasali | camlı |
| kahverengi-camli-kapi-modeli | kahverengi-camli-kapi-modeli | camlı |
| kompozit-metal-antrasit-giris-kapisi | kompozit-metal-antrasit-giris-kapisi | bina |
| kompozit-metal-giris-kapisi | kompozit-metal-giris-kapisi | bina |
| kompozit-panel-daire-giris-kapisi | kompozit-panel-daire-giris-kapisi | bina |
| kompozit-sac-panel-sol-tarafi-siyah-camli-bina-kapisi | kompozit-sac-panel-sol-tarafi-siyah-camli-bina-kapisi | camlı, bina |
| laminoks-camli-celik-kapi | laminoks-camli-celik-kapi | camlı |
| lazer-kesim-camli-bina-giris-kapisi | lazer-kesim-camli-bina-giris-kapisi | camlı, bina |
| lazer-kesim-celik-kapi-camli | lazer-kesim-celik-kapi-camli | camlı |
| lazer-kesim-is-yeri-giris-kapisi | lazer-kesim-is-yeri-giris-kapisi | bina |
| lazer-kesim-siyah-camli-celik-kapi | lazer-kesim-siyah-camli-celik-kapi | camlı |
| lazerli-apartman-giris-kapisi | lazerli-apartman-giris-kapisi | apartman, bina |
| lazerli-bina-giris-kapisi | lazerli-bina-giris-kapisi | bina |
| luks-apartman-giris-kapisi | luks-apartman-giris-kapisi | apartman, bina |
| luks-kabartmali-camli-antrasit-pvc-kabartma-celik-kapi | luks-kabartmali-camli-antrasit-pvc-kabartma-celik-kapi | camlı |
| luks-laminoks-aynali-bina-giris-kapisi | luks-laminoks-aynali-bina-giris-kapisi | camlı, bina |
| luks-pvc-kabartma-daire-ve-bina-giris-kapisi-yanyana | luks-pvc-kabartma-daire-ve-bina-giris-kapisi-yanyana | bina |
| luks-pvc-kabartma-ozel-kollu-daire-giris-kapisi | luks-pvc-kabartma-ozel-kollu-daire-giris-kapisi | bina |
| selcuklu-motifli-antrasit-apartman-kapisi | selcuklu-motifli-antrasit-apartman-kapisi | apartman |
| tek-acilir-lazerli-aynali-kapi (+ 2) | tek-acilir-lazerli-aynali-kapi, …-2 | camlı |
| thermo-woord-agac-tan-yapilmis-bina-giris-kapisi | thermo-wood-agac-tan-yapilmis-bina-giris-kapisi | bina |
| uc-acilir-selcuklu-motifli-bina-apartman-kapisi | uc-acilir-selcuklu-motifli-bina-apartman-kapisi | apartman, bina |
| uc-kanatli-beyaz-kapi-selcuklu-motifli | uc-kanatli-beyaz-kapi-selcuklu-motifli | beyaz |
| ustten-isiklikli-bina-kapisi | ustten-isiklikli-bina-kapisi | bina |
| yavru-kanat-camli-laminoks-celik-kapi | yavru-kanat-camli-laminoks-celik-kapi | camlı |
| yavru-kanatli-camli-bina-giris-kapisi | yavru-kanatli-camli-bina-giris-kapisi | camlı, bina |
| yavru-kanatli-camli-celik-kapi | yavru-kanatli-camli-celik-kapi | camlı |
| yavru-kanatli-laminoks-bina-giris-kapisi | yavru-kanatli-laminoks-bina-giris-kapisi | bina |
| yavru-kanatli-lazerli-bina-giris-kapisi | yavru-kanatli-lazerli-bina-giris-kapisi | bina |
| yavru-kanatlı-lazer-kesim-camlı-celik-kapi | yavru-kanatli-lazer-kesim-camli-celik-kapi | camlı |

Yalnız çelik kapı fiyat sayfasında duran 71 kök ad: `luks-laminoks-kapi-modeli` ile `modeli-2`–`10`, `14`–`18` ve `20`–`51` (47 dosya; 11, 12, 13 ve 19 yok), `luks-pvc-kabartma-celik-kapi-modeli` ile `modeli-2`, `5`, `6`, `7`, `9`, `10` (7 dosya), `antrasit-renkli-kapi`, `antrasit-siyah-laminoks-daire-kapisi-tek-kanatli`, `buyuk-kapi-modeli`, `genis-kapi-modeli`, `korkuluklu-bordo-renkli-kapi-modeli`, `menfezli-kapi-modeli` ve `-2`, `-3`, `metal-celik-kapi`, `parlak-siyah-high-gloss-luks-kapi`, `selcuklu-motifli-daire-kapisi`, `selcuklu-motifli-is-yeri-kapisi`, `selcuklu-motifli-kapi-modeli`, `siyah-pervazli-agac-desenli-luks-kapi`, `siyah-pervazli-gri-kanatli-kapi`, `yangin-cikis-kapisi`, `yuksek-kapi`.

### Keşif notları (Aşama 0)

- Şablon: `rehber/osmaniye-celik-kapi-fiyatlari.html`. Galeri sınıfı `gallery rehber-gallery`. Canonical biçimi `https://eminkapiosmaniye.com/...` (www yok).
- Menü ve footer her HTML'de elle durmuyor. Kaynak `partials/header.html` ve `partials/footer.html`. Sayfalara `npm run build:chrome` basıyor. Görev metni "her HTML'i elle güncelle" diyor; proje düzeni partial + basım. Projeye uyulacak.
- Rehber liste sayfası var: `rehber/index.html`. Yeni sayfa açılmayacak; bu listeye 5 kart eklenecek.
- Repoda `sitemap.xml` yok. `sitemap-images.xml` var. `robots.txt` ikisine de izin veriyor ve `/rehber/` engelli değil. Eksik `sitemap.xml` canlıda başka bir kopya olabilir; Aşama 3'te sıfırdan yazmadan önce sorulacak.
- Telefon `0542 236 236 5` ve adres `Adnan Menderes Mah. Trafo Cd. No: 6/A` sitedeki bilgiyle aynı. Metindeki "15 yılı aşkın" ifadesi anasayfadaki "15 yıllık tecrübe" ile çelişmiyor; makale metni değiştirilmeyecek.
- İç bağlantı karşılıkları birebir değil. Aşama 2'de kullanılacak öneri (onay bu planla birlikte):

| Metindeki adres | Önerilen hedef |
|---|---|
| `/osmaniye-celik-kapi/` | `urunler/celik-kapi.html` |
| `/osmaniye-kapi-modelleri/` | `urunler/index.html` |
| `/osmaniye-celik-kapi-fiyatlari/` | `rehber/osmaniye-celik-kapi-fiyatlari.html` |
| `/oda-kapi-modelleri/` | `urunler/ic-oda-kapisi.html` |
| `/luks-ic-kapi-modelleri/` | `urunler/luks-ic-kapi.html` |

Yakın ikinci adaylar da duruyor (`rehber/osmaniye-oda-kapi-modelleri.html`, `rehber/osmaniye-luks-ic-kapi-modelleri.html`, `rehber/osmaniye-en-cok-tercih-edilen-kapi-modelleri.html`). Öneri değişirse Aşama 2'den önce söylemek yeterli.

### Uygulama planı

1. **Aşama 1 — görseller.** Orijinal klasöre dokunulmaz. Kopyalar `assets/img/rehber/cift-kanatli/` altına gider (`/images/rehber/` açılmaz; sitedeki görsel kökü `assets/img/`). Adlar küçük harf, tireli, Türkçe karaktersiz. Her dosyadan WebP üretilir: uzun kenar en fazla 1600 px ve 800 px, kırpma yok, EXIF temiz. Büyük sürüm 200 KB, küçük sürüm 100 KB altında tutulur.
2. **Eşleme.** Dosya adına göre beş sayfaya dağıtılır. Bir görsel birden fazla kurala uyarsa birden fazla sayfada durabilir; aynı sayfada iki kez durmaz. Kurallara uymayanlar (numaralı laminoks / PVC serisi gibi) beş yeni sayfaya zorlanmaz. Klasördeki 129 görselin tamamı ayrıca `rehber/osmaniye-celik-kapi-fiyatlari.html` galerisine eklenir. Beyaz sayfası için adında beyaz geçen dosyalar var; görselsiz sayfa beklenmiyor.
3. **Aşama 2 — sayfalar.** Şablonun header, footer ve CSS'i kullanılır. Yeni bir galeri sistemi yazılmaz. Mevcut `rehber-gallery` ve lightbox kalır; `srcset` küçük bir eklemedir, raporda belirtilir. EK B metni aynen HTML'e çevrilir. Tablolar yatay kaydırmalı sarmalayıcıya alınır. Her sayfada tek H1, içindekiler, öne çıkan görsel, ilgili rehberler ve JSON-LD (`Article`, `BreadcrumbList`, `FAQPage`).
4. **Aşama 3 — bağlama.** Beş kısa ad menü açılır listesine ve footer rehber listesine partial üzerinden eklenir, ardından chrome basılır. `rehber/index.html` kartları güncellenir. Çelik kapı, iç oda kapısı, lake / lüks iç kapı ve anasayfadan yeni sayfalara mevcut cümleyi bozmadan birer bağlantı konur. `sitemap-images.xml` yeni görselleri alır. `sitemap.xml` ancak canlıdaki dosyanın repoda olmadığı netleşince, ayrıca onayla ele alınır.
5. **Aşama 4 — kontrol.** Kırık bağlantı, eksik görsel, tek H1, title / description uzunluğu, canonical ve JSON-LD taranır. Mobilde tablo kaydırması kontrol edilir. Kapanış raporu dosya listesi ve Search Console adımlarını içerir.

Sıra değişmez: her aşamanın sonunda kısa rapor, sonra onay. Aşama 1 görselleri hazır; Aşama 2, yukarıdaki sorular ve onay olmadan başlamaz.

---

## ÇALIŞMA KURALLARI

1. Aşamalar sırayla yapılacak. Her aşamanın sonunda kısa rapor ver ve **onayımı bekle**; onay gelmeden sonraki aşamaya geçme.
2. Emin olmadığın hiçbir bilgiyi (fiyat, garanti, süre, adres, telefon, kuruluş yılı) uydurma; soru olarak bana getir. Kendi sorduğun soruyu kendin cevaplayıp kapatma.
3. İstenmeyen hiçbir dosyayı silme, yeniden adlandırma ya da yeniden biçimlendirme.
4. Mevcut tasarımı, CSS'i ve sayfa şablonunu değiştirme; gerekirse küçük eklemeler yap ve raporda belirt.
5. Bu dosyadaki bir kural ile projedeki mevcut düzen çelişirse mevcut düzene uy ve bunu bana bildir.
6. Makale metinlerini (EK B) **aynen** kullan: cümle ekleme, çıkarma, yeniden yazma yok. Yalnızca Markdown → HTML dönüşümü ve aşağıda açıkça istenen bağlantı düzeltmeleri yapılır.

---

## AŞAMA 0 — KEŞİF (hiçbir dosyayı değiştirme)

1. Proje yapısını tara: `/rehber/` klasörü; menüde "Bilgi / Fiyat Rehberi" bölümünün nerede tanımlandığı (header, footer, ortak include ya da her sayfada tekrar eden blok); `sitemap.xml`; `robots.txt`; varsa rehber liste/index sayfası.
2. `/rehber/osmaniye-celik-kapi-fiyatlari.html` sayfasını şablon olarak incele: head yapısı, breadcrumb, schema, görsel kullanımı, CSS sınıfları.
3. Görsel klasöründeki tüm dosyaları listele: dosya adı, format, piksel boyutu, dosya boyutu.
4. Sitedeki mevcut iletişim bilgilerini (telefon, adres) ve kuruluş/tecrübe ifadesini bul.
5. **Rapor:** bulduğun yapı, menünün kaç dosyada tekrarlandığı, görsel listesi, canonical'larda kullanılan alan adı biçimi (www'li / www'siz), eksik ya da belirsiz olan her şey.

---

## AŞAMA 1 — GÖRSELLER

Orijinal klasöre **dokunma**. Görselleri proje içine kopyalayıp kopya üzerinde çalış (mevcut görsel klasörü düzenine uy; yoksa `/images/rehber/`).

### A) Yeniden adlandırma (önce bu yapılır)

- Küçük harf, tire ile ayrılmış; Türkçe karakter yok (ç→c, ğ→g, ı→i, ö→o, ş→s, ü→u); boşluk ve özel karakter yok.
- Ad, orijinal addaki bilgiyi korusun ve açıklayıcı olsun. Örnek: `cift-kanatli-bina-giris-kapisi-01.webp`, `camli-bina-kapisi-aynali-02.webp`.
- Aynı ad iki kez oluşmasın; sıra numarası ekle.
- Orijinal ad → yeni ad eşleme tablosunu rapora koy.

### B) Boyut ve format

- Format: WebP (kalite ~80). Şeffaflık gerekmiyorsa PNG bırakma.
- İki boyut üret: büyük (uzun kenar en fazla 1600 px) ve küçük (800 px). Küçük görseli büyütme.
- Hedef: büyük sürüm 200 KB altı, küçük sürüm 100 KB altı.
- EXIF/metadata temizle. En-boy oranını bozma, kırpma yapma.

### C) Sayfalarla eşleştirme (dosya ADINA göre)

| Dosya adında geçen ifade | Kullanılabileceği sayfalar |
|---|---|
| çift kanatlı / cift kanat | bina-giris-kapisi, apartman-kapisi, villa-giris-kapisi |
| cam / camlı / ayna / aynalı | camli-bina-kapisi |
| beyaz | beyaz-renkli-kapi |
| villa, apartman, bina, giriş | adı geçen sayfaya öncelikli |

- Bir görsel birden fazla kurala uyuyorsa birden fazla sayfada kullanılabilir. Aynı görseli aynı sayfada iki kez kullanma; görselleri sayfalar arasında mümkün olduğunca dağıt.
- Hiçbir kurala uymayan görselleri bir sayfaya zorla yerleştirme; listele ve bana sor.
- Bir sayfaya uygun görsel çıkmazsa (özellikle beyaz-renkli-kapi) uydurma; bana bildir.
- **Bu klasördeki TÜM görseller ayrıca `/rehber/osmaniye-celik-kapi-fiyatlari.html` sayfasında da kullanılacak** (galeri ya da içerik arası; sayfanın mevcut tasarımına uygun biçimde).

### D) HTML kullanımı

- `<img>` için `width` ve `height` öznitelikleri; `srcset` ile 800/1600 sürümleri; `loading="lazy"` (sayfanın öne çıkan ilk görseli hariç — onda `fetchpriority="high"`).
- Alt metin: dosya adından anlaşılan içeriği tarif etsin ve sayfanın odak kelimesini doğal biçimde içersin. Her alt metin farklı olsun. Öne çıkan görselin alt metni EK A tablosundaki ifade olsun.
- Addan çıkarılamayan ayrıntı (renk, malzeme, model adı, müşteri adı) ekleme.

**Rapor:** eşleme tablosu (orijinal ad → yeni ad → kullanılacağı sayfalar), önce/sonra dosya boyutları, eşleşmeyen görseller.

---

## AŞAMA 2 — 5 YENİ SAYFA

Konum: `/rehber/` altında; şablon sayfanın header, footer ve CSS'i birebir kullanılarak. SEO alanları EK A'da, metinler EK B'de.

### İçerik

- Her sayfada tek `<h1>` (EK B'deki `#` satırı). Başlık hiyerarşisini koru: `##` → H2, `###` → H3.
- Markdown tabloları `<table>` olarak, mobilde taşmayacak biçimde (yatay kaydırmalı sarmalayıcı) yerleştir.
- H1'den sonra giriş paragrafı, ardından öne çıkan görsel ve sayfa içi **içindekiler** (H2 başlıklarına çapa bağlantıları).
- İçerik arasına Aşama 1 eşlemesine göre ilgili görseller.
- Sayfa sonunda "İlgili rehberler" bloğu: diğer 4 yeni sayfa + `osmaniye-celik-kapi-fiyatlari.html`.
- Görünür breadcrumb: Anasayfa › Bilgi / Fiyat Rehberi › sayfa adı.

### Bağlantılar

- EK B'deki site içi bağlantılar eski adres biçimiyle yazıldı. Bunları projede **gerçekten var olan** karşılık sayfalarla değiştir:

| Metindeki adres | Aranacak karşılık |
|---|---|
| `/osmaniye-celik-kapi/` | çelik kapı ana sayfası |
| `/osmaniye-kapi-modelleri/` | kapı modelleri / ürünler sayfası |
| `/osmaniye-celik-kapi-fiyatlari/` | `/rehber/osmaniye-celik-kapi-fiyatlari.html` |
| `/oda-kapi-modelleri/` | iç oda kapısı modelleri sayfası |
| `/luks-ic-kapi-modelleri/` | lüks / lake iç kapı sayfası |

- Karşılığı bulunamayan bağlantıyı sessizce kaldırma; listele ve bana sor.
- Dış bağlantılar (Wikipedia, TSE) kalsın: `target="_blank" rel="noopener"`; **nofollow ekleme**.
- Telefon numarası tıklanabilir olsun (`tel:` bağlantısı).
- Metindeki telefon (0542 236 236 5) ve adres (Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye) sitedeki mevcut bilgiyle farklıysa sitedekini kullan ve bana bildir.
- "15 yılı aşkın" ifadesi sitedeki kuruluş bilgisiyle çelişiyorsa değiştirme, bana bildir.

### `<head>`

- `<title>` ve meta description: EK A'daki gibi, birebir.
- `<link rel="canonical">`: mevcut sayfalardaki alan adı biçimiyle aynı.
- Open Graph ve Twitter Card etiketleri (`og:image` = öne çıkan görselin tam URL'si).
- `lang="tr"`, viewport ve şablondaki diğer ortak etiketler.

### Yapısal veri (JSON-LD)

- `Article`: headline, description, image, datePublished, dateModified, author ve publisher = Emin Kapı.
- `BreadcrumbList`: görünür breadcrumb ile aynı.
- `FAQPage`: yalnızca sayfadaki "Sıkça Sorulan Sorular" bölümündeki soru ve cevaplarla; metin birebir aynı.
- Sayfada görünmeyen hiçbir bilgiyi (puan, yorum, fiyat) schema'ya ekleme.

### Rank Math ölçütlerinin HTML karşılığı (her sayfa için kontrol et)

- Odak kelime; title'ın başında, meta description'da, URL'de, H1'de, ilk paragrafta, en az bir H2'de ve en az bir görselin alt metninde geçiyor. (Metinler buna göre yazıldı; dönüşümde bozma.)
- Title 60, description 160 karakterin altında.
- En az bir iç bağlantı ve en az bir dofollow dış bağlantı var.
- Kısa paragraflar, içindekiler bloğu, en az bir görsel.

---

## AŞAMA 3 — SİTEYE BAĞLAMA

1. **Menü:** "Bilgi / Fiyat Rehberi" bölümünün altına 5 sayfayı ekle. Menü birden fazla HTML dosyasında tekrarlanıyorsa **hepsinde** güncelle; eksik dosya kalmasın.
2. **Footer:** rehber bağlantıları footer'da listeleniyorsa 5 sayfayı ekle (tüm sayfalarda).
3. **Rehber liste/index sayfası** varsa 5 sayfayı kart ya da liste olarak ekle; yoksa oluşturma, bana sor.
4. **`/rehber/osmaniye-celik-kapi-fiyatlari.html`:** klasördeki TÜM görselleri ekle ve 5 yeni sayfaya bağlantı ver.
5. **İç bağlantı:** ilgili mevcut sayfalardan (çelik kapı, bina giriş kapıları, iç oda kapısı, lake kapı, anasayfa) yeni sayfalara doğal bağlamda en az birer bağlantı ekle. Mevcut metni yeniden yazma; uygun bir cümleye ya da "ilgili sayfalar" alanına bağlantı koy.
6. **`sitemap.xml`:** 5 yeni URL'yi ekle (`lastmod` = bugünün tarihi); görsel eklenen fiyat sayfasının `lastmod`'unu güncelle. Görsel sitemap kullanılıyorsa yeni görselleri de ekle.
7. **`robots.txt`:** `/rehber/` ve görsel klasörünün engellenmediğini doğrula; `Sitemap:` satırının bulunduğunu kontrol et. Gereksiz değişiklik yapma.
8. Sayfa listesi tutan diğer dosyalar varsa onları da güncelle: `llms.txt`, RSS/feed, site içi arama dizini, HTML site haritası sayfası, `.htaccess` yönlendirme listesi vb.

---

## AŞAMA 4 — KONTROL VE KAPANIŞ RAPORU

- Tüm iç bağlantıları ve görsel yollarını tara: kırık bağlantı ve 404 görsel olmamalı.
- Her yeni sayfada: tek H1, benzersiz title ve description, doğru canonical, geçerli JSON-LD.
- Mobil görünümde tablo ve görsellerin taşmadığını kontrol et.
- **Rapor:** oluşturulan ve değiştirilen dosyaların tam listesi; görsel eşleme tablosunun son hali; bana sorulan ve cevapsız kalan maddeler; yayından sonra benim yapacaklarım (Search Console'da sitemap'i yeniden gönderme, 5 URL için dizin isteği).

---

# EK A — SAYFA SEO ALANLARI

| # | Dosya | Odak kelime | `<title>` | Meta description | Öne çıkan görsel alt metni |
|---|---|---|---|---|---|
| 1 | `/rehber/bina-giris-kapisi.html` | Bina Giriş Kapısı | Bina Giriş Kapısı: 7 Önemli Seçim Kriteri \| Osmaniye | Bina giriş kapısı modelleri, malzeme seçenekleri ve fiyatı etkileyen unsurlar. Osmaniye'de üretici Emin Kapı'dan ölçüye özel üretim ve montaj için arayın. | Bina giriş kapısı modeli – Emin Kapı Osmaniye |
| 2 | `/rehber/apartman-kapisi.html` | Apartman Kapısı | Apartman Kapısı Modelleri ve 5 Kritik Seçim İpucu \| Osmaniye | Apartman kapısı seçerken güvenlik, malzeme ve kilit sistemine dikkat edin. Osmaniye ve ilçelerinde Emin Kapı'dan ölçüye özel apartman kapısı üretimi. | Apartman kapısı modeli – Emin Kapı Osmaniye |
| 3 | `/rehber/villa-giris-kapisi.html` | Villa Giriş Kapısı | Villa Giriş Kapısı: 6 Şık ve Güvenli Model \| Osmaniye | Villa giriş kapısı modelleri: pivot, çift kanat ve dış iklim serisi. Osmaniye'de üretici Emin Kapı ile villanıza özel ölçü, renk ve kaplama seçenekleri. | Villa giriş kapısı modeli – Emin Kapı Osmaniye |
| 4 | `/rehber/beyaz-renkli-kapi.html` | Beyaz Renkli Kapı | Beyaz Renkli Kapı: 5 Zamansız Dekorasyon Fikri \| Emin Kapı | Beyaz renkli kapı modelleri evinizi ferah ve modern gösterir. Lake, PVC ve çelik seçenekleriyle Osmaniye Emin Kapı'dan beyaz renkli kapı çözümleri. | Beyaz renkli kapı modeli – Emin Kapı Osmaniye |
| 5 | `/rehber/camli-bina-kapisi.html` | Camlı Bina Kapısı | Camlı Bina Kapısı: 6 Güvenli ve Modern Seçenek \| Osmaniye | Camlı bina kapısı ile apartman girişiniz aydınlık ve güvenli olsun. Temperli ve lamine camlı modeller Osmaniye Emin Kapı'da; keşif için hemen arayın. | Camlı bina kapısı modeli – Emin Kapı Osmaniye |

Menü ve "İlgili rehberler" bloğunda kullanılacak kısa adlar: Bina Giriş Kapısı · Apartman Kapısı · Villa Giriş Kapısı · Beyaz Renkli Kapı · Camlı Bina Kapısı

---

# EK B — MAKALE METİNLERİ

Her makale `<!-- MAKALE n BAŞLANGIÇ -->` ile `<!-- MAKALE n BİTİŞ -->` arasındadır. Metni aynen kullan.

<!-- MAKALE 1 BAŞLANGIÇ — /rehber/bina-giris-kapisi.html -->

# Bina Giriş Kapısı Modelleri ve Seçim Rehberi

Bina giriş kapısı, bir yapıya gelen herkesin ilk gördüğü ve her gün onlarca kez kullanılan en yoğun kapıdır. Doğru seçilmiş bir bina giriş kapısı hem sakinlerin güvenliğini sağlar hem de binanın değerini ve görünümünü yükseltir. Osmaniye'de üretici firma olarak hizmet veren Emin Kapı, bu rehberde model seçerken bilmeniz gereken her şeyi sade bir dille anlatıyor.

## Bina Giriş Kapısı Nedir, Neden Önemlidir?

Bina giriş kapısı; apartman, site, iş merkezi veya rezidans gibi yapıların ana girişinde kullanılan, daire kapılarına göre daha geniş ve daha dayanıklı üretilen dış kapıdır. Gün içinde çok sık açılıp kapandığı için menteşesi, kilidi ve gövdesi yoğun kullanıma göre tasarlanır.

İyi bir giriş kapısı üç işi birden yapar: yabancıların kontrolsüz girişini engeller, yağmur ve rüzgârı dışarıda tutar ve binaya şık bir yüz kazandırır. Bu yüzden yalnızca fiyata bakarak karar vermek, birkaç yıl içinde tamir ve yenileme masrafı olarak geri döner.

## Bina Giriş Kapısı Modelleri ve Malzeme Seçenekleri

Her binanın mimarisi, kat sayısı ve bütçesi farklıdır. Bu nedenle bina giriş kapısı modelleri de malzemeye göre ayrılır.

| Malzeme | Öne çıkan yönü | Kimler için uygun |
| --- | --- | --- |
| Çelik gövdeli | Yüksek dayanım, güçlü kilit altyapısı | Güvenliği ön planda tutan apartmanlar |
| Alüminyum doğramalı | Hafif, paslanmaz, geniş cam yüzey | Modern ve aydınlık giriş isteyen binalar |
| Ferforje ve camlı | Klasik, gösterişli görünüm | Geleneksel mimariye sahip yapılar |
| Kompozit kaplamalı | Güneşe ve yağmura dayanıklı yüzey | Doğrudan dış havaya açık girişler |

### Tek Kanat mı, Çift Kanat mı?

Dar girişlerde tek kanat yeterlidir. Eşya taşıma, engelli erişimi ve yoğun insan trafiği düşünüldüğünde bir buçuk kanat veya çift kanat modeller çok daha kullanışlıdır. Emin Kapı, giriş boşluğunuza göre tek kanat, çift kanat ve pivot seçenekleri ölçüye özel üretir.

## Bina Giriş Kapısı Seçerken Dikkat Edilecek 7 Kriter

1. **Gövde ve sac kalınlığı:** Kapının ömrünü belirleyen ilk unsurdur. Kalın sac ve sağlam kasa, darbelere karşı direnç sağlar.
2. **Kilit sistemi:** Otomat karşılıklı elektrikli kilit, diafon ve görüntülü zil sistemleriyle uyumlu olmalıdır.
3. **Kapı kapatıcı:** Hidrolik kapatıcı, kapının çarpmadan ve tam olarak kapanmasını sağlar.
4. **Cam türü:** Camlı modellerde temperli veya lamine cam tercih edilmelidir.
5. **Yüzey kaplaması:** Güneş ve yağmur alan cephelerde solmaya dayanıklı boya ya da kompozit kaplama gerekir.
6. **Ölçüye uygunluk:** Hazır ölçü yerine yerinde alınan ölçüyle üretim, sızdırma ve sarkma sorunlarını önler.
7. **Montaj ve servis:** En iyi kapı bile kötü montajla sorun çıkarır; üretici firmayla çalışmak servis sürecini kolaylaştırır.

## Osmaniye'de Bina Giriş Kapısı Üretimi: Emin Kapı

Emin Kapı, Osmaniye'de 15 yılı aşkın süredir kapı üreten yerel bir firmadır. Aracı olmadan doğrudan üreticiyle çalışmak; ölçü, renk, desen ve kaplamada özgürlük, ayrıca satış sonrası hızlı servis anlamına gelir.

Osmaniye'nin sıcak yazları ve yağışlı kışları dış kapıları yorar. Bu yüzden dış cepheye bakan girişlerde [dış iklim serisi ve çelik kapı modellerimizi](https://eminkapiosmaniye.com/osmaniye-celik-kapi/) öneriyoruz. Tüm ürün gruplarını [Osmaniye kapı modelleri](https://eminkapiosmaniye.com/osmaniye-kapi-modelleri/) sayfamızda inceleyebilirsiniz.

### Hizmet Verdiğimiz Bölgeler

[Osmaniye](https://tr.wikipedia.org/wiki/Osmaniye) merkezin yanı sıra Kadirli, Düziçi, Bahçe, Toprakkale, Hasanbeyli ve Sumbas ilçelerine hizmet veriyoruz. Ceyhan, Kozan, Erzin, Dörtyol, İskenderun, Nurdağı ve İslahiye gibi çevre ilçelerden gelen talepleri de karşılıyoruz.

## Bina Giriş Kapısı Fiyatları Neye Göre Değişir?

Bina giriş kapısı fiyatları tek bir rakamla söylenemez; çünkü her kapı ölçüye göre üretilir. Fiyatı belirleyen başlıca unsurlar şunlardır:

- Kapının eni, boyu ve kanat sayısı
- Gövde malzemesi ve sac kalınlığı
- Cam miktarı ve cam türü
- Kilit, kapatıcı ve çekme kol gibi aksesuarlar
- Yüzey kaplaması ve özel renk tercihi
- Montajın yapılacağı adres

Net fiyat için giriş boşluğunun ölçüsünü ve beğendiğiniz modeli bize iletmeniz yeterlidir. Çelik modeller için [Osmaniye çelik kapı fiyatları](https://eminkapiosmaniye.com/osmaniye-celik-kapi-fiyatlari/) sayfamıza da göz atabilirsiniz.

## Sıkça Sorulan Sorular

### Bina giriş kapısı kaç günde teslim edilir?

Süre; modele, ölçüye ve üretim yoğunluğuna göre değişir. Ölçü alındıktan sonra size net bir teslim tarihi veriyoruz.

### Mevcut kapıyı söküp yenisini takıyor musunuz?

Evet. Eski kapının sökümü ve yeni kapının montajı ekibimiz tarafından aynı ziyarette yapılır.

### Apartman yönetimi olarak toplu teklif alabilir miyiz?

Elbette. Birden fazla blok veya giriş için yerinde keşif yapıp yönetime yazılı teklif sunuyoruz.

## Bina Giriş Kapısı İçin Bize Ulaşın

Binanıza yakışan, uzun yıllar sorunsuz kullanacağınız bir bina giriş kapısı için Emin Kapı'yı arayın: **0542 236 236 5**. Fabrikamız Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye adresindedir; modelleri yerinde görmek için bekleriz.

<!-- MAKALE 1 BİTİŞ -->

<!-- MAKALE 2 BAŞLANGIÇ — /rehber/apartman-kapisi.html -->

# Apartman Kapısı Modelleri ve Fiyatını Belirleyen Unsurlar

Apartman kapısı, bir binada yaşayan herkesin ortak güvenlik noktasıdır. Sağlam bir apartman kapısı hırsızlığa karşı ilk engeli oluşturur, soğuğu ve gürültüyü dışarıda bırakır, binaya da bakımlı bir görünüm kazandırır. Osmaniye'de üretim yapan Emin Kapı olarak, doğru modeli seçmenize yardımcı olacak bilgileri bu yazıda topladık.

## Apartman Kapısı Çeşitleri Nelerdir?

Günlük dilde apartman kapısı iki farklı ürün için kullanılır. İkisinin ihtiyacı birbirinden farklıdır, bu yüzden önce hangisini aradığınızı netleştirmek gerekir.

### Apartman Ana Giriş Kapısı

Binanın sokağa açılan kapısıdır. Gün boyu çok sık kullanıldığı için güçlü menteşe, hidrolik kapatıcı ve otomatla açılan elektrikli kilit ister. Genellikle camlı, çelik gövdeli veya alüminyum doğramalı üretilir.

### Apartman Daire Kapısı

Her dairenin kendi giriş kapısıdır ve bugün neredeyse tamamı çelik kapıdır. Burada öncelik çok noktadan kilitleme, ses ve ısı yalıtımı ile iç dekorasyona uyan kaplamadır. Daire girişleri için [Osmaniye çelik kapı](https://eminkapiosmaniye.com/osmaniye-celik-kapi/) modellerimizi inceleyebilirsiniz.

## Apartman Kapısı Seçerken Dikkat Edilecek 5 Nokta

1. **Güvenlik seviyesi:** Sac kalınlığı, kasa yapısı ve kilit sayısı kapının direncini belirler. Zemin kat ve giriş kapılarında bu konu daha da önemlidir.
2. **Kilit ve geçiş sistemi:** Ana girişte diafonla uyumlu elektrikli kilit; dairelerde çok noktadan kilitlenen, kopyalanması zor anahtarlı silindir tercih edilmelidir.
3. **Yalıtım:** Kaliteli fitil ve dolgu, merdiven boşluğundan gelen sesi ve soğuğu belirgin biçimde azaltır.
4. **Dış etkenlere dayanım:** Güneş ve yağmur alan girişlerde solmayan, şişmeyen yüzey kaplaması gerekir.
5. **Ölçüye özel üretim:** Eski binalarda kapı boşlukları standart değildir. Yerinde ölçü alınmadan üretilen kapı, sürtme ve boşluk sorunlarına yol açar.

## Apartman Kapısı Modelleri: Hangi Malzeme Daha İyi?

| Model | Güçlü yönü | Dikkat edilecek nokta |
| --- | --- | --- |
| Çelik apartman kapısı | En yüksek güvenlik, uzun ömür | Dış cephede kaplama türü doğru seçilmeli |
| Camlı apartman kapısı | Aydınlık ve ferah giriş | Cam temperli veya lamine olmalı |
| Alüminyum doğramalı | Hafif, paslanmaz, modern | Kilit altyapısı güçlendirilmeli |
| Ferforje süslemeli | Klasik ve gösterişli | Boya bakımı düzenli yapılmalı |

Tek bir doğru cevap yoktur. Kalabalık ve işlek bir sokakta çelik gövde öne çıkarken, karanlık bir merdiven holü için camlı model daha doğru bir seçimdir. Bina girişlerine özel seçenekler için [Osmaniye kapı modelleri](https://eminkapiosmaniye.com/osmaniye-kapi-modelleri/) sayfamıza bakabilirsiniz.

## Apartman Kapısı Fiyatları Nasıl Belirlenir?

Apartman kapısı fiyatları ölçüye ve seçilen donanıma göre değişir. Aynı model, iki farklı binada farklı fiyata çıkabilir. Fiyatı etkileyen başlıca kalemler:

- Kapı ölçüsü ve kanat sayısı
- Gövde malzemesi ve sac kalınlığı
- Kilit tipi, kapatıcı ve çekme kol
- Cam yüzeyin büyüklüğü ve cam türü
- Kaplama, renk ve desen tercihi
- Söküm, montaj ve nakliye

Karşılaştırma yapabilmeniz için [Osmaniye çelik kapı fiyatları](https://eminkapiosmaniye.com/osmaniye-celik-kapi-fiyatlari/) sayfamızı da hazırladık. En doğru fiyat ise yerinde alınan ölçüyle verilir.

## Osmaniye'de Apartman Kapısı İçin Neden Emin Kapı?

Emin Kapı, Osmaniye'de 15 yılı aşkın süredir çelik kapı ve iç oda kapısı üreten yerel bir firmadır. Üretici olduğumuz için renk, desen ve ölçüde hazır ürünle sınırlı kalmazsınız; ayrıca satış sonrası servise ihtiyaç duyduğunuzda muhatabınız aynı şehirdedir.

[Osmaniye](https://tr.wikipedia.org/wiki/Osmaniye) merkez, Kadirli, Düziçi, Bahçe, Toprakkale, Hasanbeyli ve Sumbas'ta montaj yapıyoruz. Ceyhan, Kozan, Erzin, Dörtyol, Nurdağı ve İslahiye gibi komşu ilçelerdeki apartman yönetimlerine ve müteahhitlere de hizmet veriyoruz.

## Sıkça Sorulan Sorular

### Apartman kapısı değişimi için tüm kat maliklerinin onayı gerekir mi?

Ana giriş kapısı ortak alan sayıldığı için karar apartman yönetimi veya kat malikleri kurulu tarafından alınır. Daire kapınızı ise kendiniz yeniletebilirsiniz; yalnızca dış yüzeyin binanın genel görünümüne uygun olması beklenir.

### Eski apartman kapısı aynı gün değişir mi?

Kapı önceden ölçüye göre üretildiği için söküm ve montaj çoğu zaman aynı gün içinde tamamlanır. Bina o gece kapısız kalmaz.

### Diafon ve otomat sistemimiz yeni kapıya uyar mı?

Evet. Ölçü sırasında mevcut sisteminize bakıyor, kilidi buna uygun seçiyoruz.

## Apartman Kapısı İçin Hemen Bilgi Alın

Binanıza ya da dairenize uygun apartman kapısı için Emin Kapı'yı arayın: **0542 236 236 5**. Fabrikamız Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye adresindedir.

<!-- MAKALE 2 BİTİŞ -->

<!-- MAKALE 3 BAŞLANGIÇ — /rehber/villa-giris-kapisi.html -->

# Villa Giriş Kapısı Modelleri: Şıklık ve Güvenlik Bir Arada

Villa giriş kapısı, evinizin karakterini daha bahçe kapısından girerken anlatan en önemli mimari parçadır. Apartman dairelerinden farklı olarak villa giriş kapısı doğrudan güneşe, yağmura ve dışarıdan gelebilecek tehditlere açıktır; bu yüzden hem gösterişli hem de çok sağlam olmak zorundadır. Osmaniye'de üretici olan Emin Kapı, villanıza en uygun modeli seçmeniz için bilmeniz gerekenleri derledi.

## Villa Giriş Kapısı Neden Farklıdır?

Bir daire kapısı kapalı ve korunaklı bir merdiven holüne açılır. Villa giriş kapısı ise dört mevsim açık havayla temas eder ve çoğu zaman sokaktan görülür. Bu fark üç ihtiyacı beraberinde getirir:

- **Daha yüksek güvenlik:** Müstakil evlerde komşu daire ya da kapıcı yoktur; kapı tek başına caydırıcı olmalıdır.
- **Hava koşullarına dayanım:** Yüzey güneşte solmamalı, yağmurda şişmemeli ve paslanmamalıdır.
- **Mimariyle uyum:** Kapı; cephe kaplaması, pencere doğramaları ve bahçe düzeniyle bir bütün oluşturmalıdır.

## Villa Giriş Kapısı Modelleri: 6 Şık Seçenek

1. **Pivot kapı:** Kenardan değil, alt ve üst milden döner. Çok geniş ve yüksek kanatlara izin verdiği için modern villaların gözdesidir.
2. **Çift kanat kapı:** Geniş girişlerde simetrik ve görkemli bir görünüm sağlar; eşya taşımayı kolaylaştırır.
3. **Bir buçuk kanat kapı:** Günlük kullanımda tek kanat açılır, gerektiğinde yan kanat da devreye girer.
4. **Yan ve üst camlı kapı:** Sabit cam paneller girişe gün ışığı alır ve kapıyı olduğundan büyük gösterir.
5. **Kompozit kaplamalı kapı:** Dış hava koşullarına karşı özel üretilen yüzeyiyle uzun yıllar ilk günkü rengini korur.
6. **Ahşap görünümlü çelik kapı:** Çeliğin güvenliğini doğal ahşap sıcaklığıyla birleştirir; taş ve tuğla cephelerle çok iyi uyum sağlar.

Bu modellerin tamamı ölçüye, renge ve desene göre özelleştirilebilir. Mevcut tasarımlarımızı [Osmaniye kapı modelleri](https://eminkapiosmaniye.com/osmaniye-kapi-modelleri/) sayfasında görebilirsiniz.

## Villa Giriş Kapısı Seçerken Nelere Dikkat Edilmeli?

### Dış İklim Dayanımı

Osmaniye'de yazlar sıcak ve nemli, kışlar yağışlı geçer. Doğrudan güneş alan bir villa girişinde sıradan bir kaplama birkaç yılda solar ve kabarır. Bu nedenle dış cepheye bakan kapılarda dış iklim serisi tercih edilmelidir.

### Kilit ve Güvenlik Donanımı

Çok noktadan kilitleme, kırılmaya ve çekmeye dayanıklı silindir ile çelik kasa temel donanımdır. İsteyenler için parmak izi, şifre veya kartla açılan akıllı kilit seçenekleri de kapıya uygulanabilir.

### Isı ve Ses Yalıtımı

Giriş kapısı, evin ısı kaybettiği başlıca noktalardan biridir. Dolgulu kanat ve çift fitil sistemi hem faturanızı hem de dışarıdan gelen gürültüyü azaltır.

### Ölçü ve Oran

Yüksek tavanlı bir villaya standart ölçülü kapı küçük kalır. Kapının genişliği ve yüksekliği cepheyle orantılı olmalı; gerekirse yan ve üst sabit panellerle desteklenmelidir.

## Osmaniye'de Villa Giriş Kapısı Üretimi

Emin Kapı, Osmaniye'de 15 yılı aşkın süredir kapı üreten yerel bir firmadır. Villa projelerinde mimarınızın çizimine ya da beğendiğiniz bir fotoğrafa göre özel üretim yapıyoruz. Dış girişler için [çelik kapı ve dış iklim serimizi](https://eminkapiosmaniye.com/osmaniye-celik-kapi/), evin içi için [oda kapı modellerimizi](https://eminkapiosmaniye.com/oda-kapi-modelleri/) aynı çatı altında bulabilirsiniz. Böylece dış kapı ile iç kapılar arasında renk ve tarz bütünlüğü sağlanır.

[Osmaniye](https://tr.wikipedia.org/wiki/Osmaniye) merkez ve Kadirli, Düziçi, Bahçe, Toprakkale, Hasanbeyli, Sumbas ilçelerindeki villa, bağ evi ve müstakil evlere hizmet veriyoruz. Ceyhan, Kozan, Erzin, Dörtyol ve İskenderun gibi çevre ilçelerdeki projeler için de keşfe geliyoruz.

## Villa Giriş Kapısı Fiyatları

Villa giriş kapısı fiyatları; ölçüye, kanat tipine, kaplamaya ve kilit donanımına göre belirlenir. Pivot ve çift kanat modeller, daha fazla malzeme ve özel mekanizma gerektirdiği için tek kanat modellere göre daha yüksek bütçe ister. Akıllı kilit, yan cam paneller ve özel renk gibi tercihler de fiyata yansır.

Net rakam için giriş boşluğunun ölçüsü ve istediğiniz model yeterlidir. Genel bir fikir edinmek isterseniz [Osmaniye çelik kapı fiyatları](https://eminkapiosmaniye.com/osmaniye-celik-kapi-fiyatlari/) sayfamıza bakabilirsiniz.

## Sıkça Sorulan Sorular

### Villa giriş kapısı güneşte solar mı?

Dış ortam için üretilmeyen kaplamalar zamanla solar. Dış iklim serisi kapılarda yüzey, güneş ve yağmura dayanacak şekilde seçilir.

### İnşaat aşamasındaki villam için ne zaman ölçü aldırmalıyım?

Kaba inşaat bittikten ve kapı boşluğu netleştikten sonra ölçü alınması en doğrusudur. Montaj ise zemin kaplaması ve dış sıva tamamlandığında yapılır.

### Akıllı kilit sonradan eklenebilir mi?

Çoğu modelde eklenebilir; ancak baştan planlamak hem görünüm hem de maliyet açısından daha avantajlıdır.

## Villa Giriş Kapısı İçin Bizi Arayın

Evinize yakışan villa giriş kapısı için Emin Kapı'ya ulaşın: **0542 236 236 5**. Modelleri yerinde görmek isterseniz fabrikamız Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye adresindedir.

<!-- MAKALE 3 BİTİŞ -->

<!-- MAKALE 4 BAŞLANGIÇ — /rehber/beyaz-renkli-kapi.html -->

# Beyaz Renkli Kapı Modelleri ve Dekorasyon Fikirleri

Beyaz renkli kapı, modası hiç geçmeyen ve her dekorasyon tarzına uyum sağlayan en güvenli tercihtir. Küçük bir odayı ferah, karanlık bir koridoru aydınlık gösteren beyaz renkli kapı, bu yüzden yeni yapılan ve yenilenen evlerde en çok sorulan modellerin başında gelir. Osmaniye'de üretim yapan Emin Kapı olarak, beyaz kapı almadan önce bilmeniz gerekenleri bu yazıda bir araya getirdik.

## Beyaz Renkli Kapı Neden Bu Kadar Çok Tercih Ediliyor?

Beyaz, ışığı yansıtan bir renktir. Bu basit özellik, kapıyı dekorasyonun en kullanışlı parçalarından biri hâline getirir.

- **Mekânı büyütür:** Açık renk yüzeyler duvarla bütünleşir ve odayı olduğundan geniş gösterir.
- **Her renge uyar:** Duvar boyasını, parkeyi ya da mobilyayı değiştirdiğinizde kapıyı değiştirmeniz gerekmez.
- **Zamansızdır:** Trend renkler birkaç yılda eskir; beyaz her dönemde güncel kalır.
- **Evin değerini artırır:** Ferah ve bakımlı görünen ev, satışta ve kiralamada daha çok ilgi görür.

## Beyaz Renkli Kapı Modelleri ve Malzeme Seçenekleri

Aynı beyaz, farklı malzemede farklı sonuç verir. Kullanım yerine göre doğru malzemeyi seçmek, kapının yıllar sonraki görünümünü belirler.

| Model | Kullanım yeri | Öne çıkan özelliği |
| --- | --- | --- |
| Beyaz lake kapı | Oda, salon, yatak odası | Pürüzsüz boyalı yüzey, en şık görünüm |
| Beyaz PVC kaplı kapı | Banyo, mutfak, kiralık daireler | Neme dayanıklı, kolay silinir, ekonomik |
| Beyaz Amerikan panel kapı | Bütçe dostu projeler | Hafif, hızlı üretim, uygun fiyat |
| Beyaz camlı iç kapı | Salon, mutfak, koridor | Odalar arasında ışık geçişi sağlar |
| Beyaz çelik kapı | Daire ve villa girişi | Güvenlik ile aydınlık görünümü birleştirir |

### Beyaz Lake Kapı

Beyaz denince akla ilk gelen modeldir. MDF gövde üzerine kat kat uygulanan lake boya, mat ya da parlak pürüzsüz bir yüzey verir. Düz, derzli veya çıtalı desen seçenekleriyle hem modern hem klasik evlere uyar. Ayrıntılı bilgi için [lüks iç kapı modelleri](https://eminkapiosmaniye.com/luks-ic-kapi-modelleri/) sayfamıza bakabilirsiniz.

### Beyaz Çelik Kapı

Dış kapıda beyaz, son yıllarda özellikle modern apartman ve villalarda öne çıkıyor. İç yüzü beyaz, dış yüzü farklı renkte üretim de mümkündür; böylece kapı içeride oda kapılarıyla, dışarıda bina cephesiyle uyum sağlar. Seçenekler için [Osmaniye çelik kapı](https://eminkapiosmaniye.com/osmaniye-celik-kapi/) sayfamızı inceleyin.

## Beyaz Renkli Kapı ile 5 Zamansız Dekorasyon Fikri

1. **Beyaz kapı ve açık meşe parke:** İskandinav tarzının klasik eşleşmesidir; evi sıcak ve aydınlık gösterir.
2. **Beyaz kapı ve koyu zemin:** Antrasit ya da ceviz tonlu zeminle güçlü bir kontrast oluşturur.
3. **Siyah kapı kolu:** Mat siyah kol ve menteşe, sade beyaz kapıya modern bir karakter kazandırır.
4. **Renkli duvar önünde beyaz kapı:** Yeşil, lacivert veya toprak tonlu duvarlarda kapı ve pervaz bir çerçeve gibi öne çıkar.
5. **Kapı, süpürgelik ve pervaz aynı beyazda:** Tüm doğramalar aynı tonda olduğunda ev çok daha derli toplu görünür.

Kapıyla birlikte zemin de yenilenecekse, parke ve kapı rengini aynı anda seçmek en doğru sonucu verir. Emin Kapı'da iç kapı, mutfak dolabı ve laminat parkeyi aynı yerden seçebilirsiniz.

## Beyaz Renkli Kapı Sararır mı, Nasıl Temizlenir?

En sık sorulan soru budur. Kaliteli boya ve kaplama kullanılan bir beyaz renkli kapı, doğru bakımla uzun yıllar rengini korur. Sararmanın başlıca nedenleri düşük kaliteli boya, sürekli doğrudan güneş ve yanlış temizlik malzemesidir.

Bakım için birkaç basit kural yeterlidir:

- Nemli, yumuşak bir bezle ve gerekirse az miktarda arap sabunuyla silin.
- Çamaşır suyu, tiner ve aşındırıcı krem temizleyicilerden uzak durun.
- Tel sünger ya da sert fırça kullanmayın; yüzeyi çizer ve matlaştırır.
- Kol çevresindeki el izlerini biriktirmeden temizleyin.

Islak hacimlerde, yani banyo ve tuvalette, lake yerine neme dayanıklı PVC kaplı model seçmek daha doğrudur.

## Osmaniye'de Beyaz Renkli Kapı Üretimi: Emin Kapı

Emin Kapı, Osmaniye'de 15 yılı aşkın süredir iç oda kapısı ve çelik kapı üreten yerel bir firmadır. Kapılarınız duvar kalınlığınıza ve kapı boşluğunuza göre ölçüye özel üretilir; kırık beyaz, krem ya da saf beyaz gibi ton tercihleriniz dikkate alınır. Tüm seçenekleri [oda kapı modelleri](https://eminkapiosmaniye.com/oda-kapi-modelleri/) sayfamızda bulabilirsiniz.

[Osmaniye](https://tr.wikipedia.org/wiki/Osmaniye) merkez ile Kadirli, Düziçi, Bahçe, Toprakkale, Hasanbeyli ve Sumbas ilçelerine montaj yapıyoruz. Ceyhan, Kozan, Erzin, Dörtyol ve Nurdağı gibi komşu ilçelerdeki konut projelerine de toplu üretimle hizmet veriyoruz.

## Sıkça Sorulan Sorular

### Beyaz kapı çabuk kirlenir mi?

Kir beyazda daha kolay fark edilir, ancak pürüzsüz lake ve PVC yüzeyler nemli bezle saniyeler içinde temizlenir.

### Evdeki tüm kapılar beyaz olmak zorunda mı?

Hayır. Oda kapıları beyaz, giriş kapısının iç yüzü ahşap tonunda olabilir. Önemli olan ton ve kol uyumudur.

### Lake mi, PVC mi tercih etmeliyim?

Görünüm önceliğinizse lake; bütçe ve neme dayanım önceliğinizse PVC daha uygundur. Çoğu evde ikisi birlikte kullanılır.

## Beyaz Renkli Kapı İçin Bize Ulaşın

Evinize en uygun beyaz renkli kapı modelini birlikte seçelim. Emin Kapı'yı arayın: **0542 236 236 5**. Fabrikamız Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye adresindedir.

<!-- MAKALE 4 BİTİŞ -->

<!-- MAKALE 5 BAŞLANGIÇ — /rehber/camli-bina-kapisi.html -->

# Camlı Bina Kapısı Modelleri: Aydınlık ve Güvenli Girişler

Camlı bina kapısı, apartman girişlerini karanlık ve kapalı görünümden kurtaran en etkili çözümdür. Doğru camla üretilen bir camlı bina kapısı gün ışığını içeri alır, girişi ferah gösterir ve güvenlikten ödün vermez. Osmaniye'de üretici firma Emin Kapı, bu yazıda cam türlerinden model seçimine kadar merak edilenleri anlatıyor.

## Camlı Bina Kapısı Nedir, Hangi Avantajları Sağlar?

Camlı bina kapısı; çelik, alüminyum veya ferforje bir gövdenin içine güvenlik camı yerleştirilerek üretilen bina ana giriş kapısıdır. Tam sac kapılara göre şu avantajları sunar:

- **Aydınlık giriş:** Gündüz saatlerinde merdiven holünde lamba yakma ihtiyacını azaltır.
- **Güven hissi:** Kapıyı açmadan dışarıda kimin olduğunu görürsünüz.
- **Şık görünüm:** Cam ve metal birlikteliği binaya modern ve bakımlı bir yüz kazandırır.
- **Ferahlık:** Dar girişler, cam sayesinde olduğundan geniş algılanır.

## Camlı Bina Kapısı İçin Cam Türleri

Bu kapılarda en kritik konu camın türüdür. Normal pencere camı bina girişinde kesinlikle kullanılmamalıdır.

| Cam türü | Özelliği | Önerilen kullanım |
| --- | --- | --- |
| Temperli cam | Darbeye dayanıklıdır; kırılırsa küçük ve keskin olmayan parçalara ayrılır | Yoğun kullanılan tüm girişler |
| Lamine cam | İki cam arasındaki film sayesinde kırılsa bile dağılmaz | Güvenliğin öncelikli olduğu zemin kat girişleri |
| Buzlu veya desenli cam | Işığı geçirir, içerisi net görünmez | Mahremiyet istenen binalar |
| Reflekte cam | Güneş ışığını yansıtır, içeriyi daha serin tutar | Güney ve batı cepheli girişler |

Temperli ve lamine özellik aynı camda birleştirilebilir. Cam güvenliği konusunda ürünlerin [TSE](https://www.tse.org.tr) standartlarına uygun olmasına dikkat edilmelidir.

## Camlı Bina Kapısı Modelleri: 6 Güvenli ve Modern Seçenek

1. **Çelik gövdeli camlı kapı:** Sağlam çelik çerçeve içine dar ya da geniş cam şeritler yerleştirilir; güvenlik ile ışığı dengeler.
2. **Alüminyum doğramalı camlı kapı:** İnce profilleri sayesinde en geniş cam yüzeyi sunar; paslanmaz ve hafiftir.
3. **Ferforje korumalı camlı kapı:** Camın önündeki demir işçiliği hem süs hem ek güvenlik sağlar.
4. **Yan sabit panelli kapı:** Kanadın yanında sabit cam bölme bulunur; geniş giriş boşluklarını değerlendirir.
5. **Üst vasistas camlı kapı:** Kapının üstündeki cam bölüm, yüksek girişlerde ek ışık ve havalandırma verir.
6. **Kompozit kaplamalı camlı kapı:** Ahşap görünümlü dış yüzeyi camla birleştirir; güneşe ve yağmura dayanıklıdır.

Bina girişine özel tasarımlarımızı [Osmaniye kapı modelleri](https://eminkapiosmaniye.com/osmaniye-kapi-modelleri/) sayfasında inceleyebilirsiniz.

## Camlı Bina Kapısı Güvenli mi?

Doğru üretildiğinde evet. Güvenliği belirleyen camın kendisinden çok, kapının bütün olarak nasıl tasarlandığıdır.

### Güvenliği Artıran Detaylar

- Temperli ya da lamine güvenlik camı kullanılması
- Camın, elin kilide ulaşamayacağı şekilde konumlandırılması
- Sağlam kasa ve güçlü menteşe
- Otomat ve diafonla uyumlu elektrikli kilit
- Kapının her seferinde tam kapanmasını sağlayan hidrolik kapatıcı
- İsteğe bağlı ferforje ya da paslanmaz korkuluk

Bu detaylar bir araya geldiğinde camlı model, tam kapalı bir kapı kadar caydırıcı olur. Daire girişlerinde güvenliği tamamlamak için [Osmaniye çelik kapı](https://eminkapiosmaniye.com/osmaniye-celik-kapi/) modellerimize de göz atabilirsiniz.

## Osmaniye'de Camlı Bina Kapısı Üretimi ve Montajı

Emin Kapı, Osmaniye'de 15 yılı aşkın süredir kapı üreten yerel bir firmadır. Apartman yönetimleri ve müteahhitler için yerinde ölçü alıyor, cam türünü ve modeli binanın cephesine göre birlikte belirliyoruz. Osmaniye'nin sıcak yazlarında güneş alan girişler için reflekte cam ve dış iklime dayanıklı kaplama öneriyoruz.

[Osmaniye](https://tr.wikipedia.org/wiki/Osmaniye) merkezin yanında Kadirli, Düziçi, Bahçe, Toprakkale, Hasanbeyli ve Sumbas ilçelerine hizmet veriyoruz. Ceyhan, Kozan, Erzin, Dörtyol, Nurdağı ve İslahiye gibi çevre ilçelerdeki binalar için de keşfe geliyoruz.

## Camlı Bina Kapısı Fiyatları Neye Göre Değişir?

Camlı bina kapısı fiyatları ölçüye göre hesaplanır. Başlıca etkenler şunlardır:

- Kapı ölçüsü, kanat sayısı ve sabit panel olup olmadığı
- Cam türü, kalınlığı ve toplam cam alanı
- Gövde malzemesi: çelik, alüminyum veya ferforje
- Kilit, kapatıcı ve çekme kol donanımı
- Kaplama ve renk tercihi

Karşılaştırma için [Osmaniye çelik kapı fiyatları](https://eminkapiosmaniye.com/osmaniye-celik-kapi-fiyatlari/) sayfamıza bakabilir, net teklif için ölçünüzü bize iletebilirsiniz.

## Sıkça Sorulan Sorular

### Cam kırılırsa tüm kapı mı değişir?

Hayır. Yalnızca kırılan cam aynı ölçüde yenilenir; gövde ve kilit yerinde kalır.

### Dışarıdan içerisi görünür mü?

Buzlu, desenli veya reflekte cam seçildiğinde ışık içeri girer, ancak içerisi net görünmez.

### Mevcut demir kapımıza cam taktırabilir miyiz?

Bazı kapılarda mümkündür, fakat eski gövdenin durumu belirleyicidir. Çoğu zaman yeni bir kapı daha güvenli ve uzun ömürlü sonuç verir.

## Camlı Bina Kapısı İçin Teklif Alın

Binanızı aydınlatacak ve güvenle kullanacağınız camlı bina kapısı için Emin Kapı'yı arayın: **0542 236 236 5**. Fabrikamız Adnan Menderes Mah. Trafo Cd. No: 6/A Osmaniye adresindedir.

<!-- MAKALE 5 BİTİŞ -->

---

**SONRAKİ ADIM:** Dört aşama tamam. Yayına almak için commit ve push ayrı onay ister. `sitemap.xml` repoda yok. Apartman sayfasının başlığı EK A’da 60 karakter; kısaltılmadı. Makale metinlerine (EK B) dokunulmadı.
