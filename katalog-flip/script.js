/*
 * Page-flip catalog — PDF only (client-side raster via pdf.js).
 * Replace katalog-flip/pdf/*.pdf and update PDF_URL when the catalog changes.
 */

const PDF_URL = 'katalog-flip/pdf/emin_kapi_2026_katalog.pdf';
const PDF_RENDER_LONG_SIDE = 1500; // px — raster resolution per page (quality vs. memory)
const PDFJS_WORKER_URL = 'katalog-flip/vendor/pdf.worker.min.js';

// ---------- sound ----------
let audioCtx = null;
let soundOn = localStorage.getItem('flipbook-sound') !== 'off';

function ensureAudio() {
  if (!audioCtx) {
    const Ctx = window.AudioContext || window.webkitAudioContext;
    audioCtx = new Ctx();
  }
  if (audioCtx.state === 'suspended') audioCtx.resume();
  return audioCtx;
}

function playFlipSound() {
  if (!soundOn) return;
  const ctx = ensureAudio();
  const dur = 0.32 + Math.random() * 0.08;
  const bufferSize = Math.floor(ctx.sampleRate * dur);
  const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < bufferSize; i++) {
    const decay = Math.pow(1 - i / bufferSize, 2.2);
    data[i] = (Math.random() * 2 - 1) * decay;
  }

  const noise = ctx.createBufferSource();
  noise.buffer = buffer;

  const bandpass = ctx.createBiquadFilter();
  bandpass.type = 'bandpass';
  const startFreq = 1800 + Math.random() * 900;
  bandpass.frequency.setValueAtTime(startFreq, ctx.currentTime);
  bandpass.frequency.exponentialRampToValueAtTime(500, ctx.currentTime + dur);
  bandpass.Q.value = 0.7;

  const gain = ctx.createGain();
  gain.gain.setValueAtTime(0.0001, ctx.currentTime);
  gain.gain.linearRampToValueAtTime(0.6, ctx.currentTime + 0.015);
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);

  noise.connect(bandpass).connect(gain).connect(ctx.destination);
  noise.start();
  noise.stop(ctx.currentTime + dur);
}

// ---------- PDF -> page images ----------
async function renderPdfToImages(url, onProgress) {
  if (typeof pdfjsLib === 'undefined') {
    throw new Error('pdf.js yüklenemedi');
  }
  pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS_WORKER_URL;
  const pdf = await pdfjsLib.getDocument(url).promise;
  const images = [];

  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const base = page.getViewport({ scale: 1 });
    const scale = PDF_RENDER_LONG_SIDE / Math.max(base.width, base.height);
    const viewport = page.getViewport({ scale });

    const canvas = document.createElement('canvas');
    canvas.width = Math.round(viewport.width);
    canvas.height = Math.round(viewport.height);
    const ctx = canvas.getContext('2d');
    await page.render({ canvasContext: ctx, viewport }).promise;

    images.push(canvas.toDataURL('image/jpeg', 0.85));
    onProgress && onProgress(i, pdf.numPages);
    page.cleanup();
  }
  return images;
}

// The page-flip canvas clears itself to flat white before drawing each
// frame; anywhere no page is drawn on top (the lone cover slot, the thin
// spine seam) that white shows straight through. We swap it for a dark
// anthracite tone with a faint plaster-like speckle so it blends with the
// book instead of flashing white.
function createStuccoPattern(ctx) {
  const size = 256;
  const tile = document.createElement('canvas');
  tile.width = size;
  tile.height = size;
  const tctx = tile.getContext('2d');

  tctx.fillStyle = '#34383e';
  tctx.fillRect(0, 0, size, size);

  // Speckle drawn with wrap-around so edges tile seamlessly (no grid lines).
  const dot = (x, y, r, alpha, shade) => {
    tctx.fillStyle = `rgba(${shade},${shade},${shade},${alpha})`;
    tctx.beginPath();
    tctx.arc(x, y, r, 0, Math.PI * 2);
    tctx.fill();
  };
  for (let i = 0; i < 2200; i++) {
    const x = Math.random() * size;
    const y = Math.random() * size;
    const r = Math.random() * 1.1 + 0.2;
    const shade = Math.random() < 0.5 ? 255 : 0;
    const alpha = Math.random() * 0.045 + 0.012;
    dot(x, y, r, alpha, shade);
    // wrap near edges so the tile repeats without a visible seam
    if (x < 4) dot(x + size, y, r, alpha, shade);
    if (x > size - 4) dot(x - size, y, r, alpha, shade);
    if (y < 4) dot(x, y + size, r, alpha, shade);
    if (y > size - 4) dot(x, y - size, r, alpha, shade);
  }

  return ctx.createPattern(tile, 'repeat');
}

function applyStuccoBackground(pageFlip) {
  const render = pageFlip.render;
  if (!render || !render.ctx || !render.canvas) return;
  const pattern = createStuccoPattern(render.ctx);
  render.clear = function () {
    this.ctx.save();
    this.ctx.fillStyle = pattern;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.restore();
  };
}

function measureImage(src) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve({ w: img.naturalWidth, h: img.naturalHeight });
    img.onerror = () => resolve({ w: 520, h: 734 });
    img.src = src;
  });
}

// ---------- loading overlay ----------
const overlay = {
  el: null,
  bar: null,
  label: null,
  show() { this.el && this.el.classList.remove('hidden'); },
  hide() { this.el && this.el.classList.add('hidden'); },
  set(current, total, text) {
    if (!this.el) return;
    if (this.label) this.label.textContent = text || `Sayfalar hazırlanıyor… ${current}/${total}`;
    if (this.bar) this.bar.style.width = `${total ? (current / total) * 100 : 0}%`;
  },
  fail(message) {
    if (!this.el) return;
    this.el.classList.add('is-error');
    this.el.classList.remove('hidden');
    if (this.label) {
      this.label.innerHTML = `${message}<br /><a class="loading-fallback" href="${PDF_URL}" target="_blank" rel="noopener">PDF olarak aç / indir</a>`;
    }
    if (this.bar) this.bar.style.width = '0%';
    const spinner = this.el.querySelector('.spinner');
    if (spinner) spinner.style.display = 'none';
  },
};

// ---------- flipbook ----------
document.addEventListener('DOMContentLoaded', async () => {
  overlay.el = document.getElementById('loadingOverlay');
  overlay.bar = document.getElementById('loadingBar');
  overlay.label = document.getElementById('loadingLabel');

  overlay.show();
  overlay.set(0, 0, 'Katalog PDF yükleniyor…');

  let images;
  try {
    images = await renderPdfToImages(PDF_URL, (cur, total) => overlay.set(cur, total));
  } catch (err) {
    console.error('PDF yüklenemedi:', err);
    const viaFile = location.protocol === 'file:';
    overlay.fail(
      viaFile
        ? 'Yerel dosya olarak açılamaz. Basit bir HTTP sunucusu ile açın veya PDF’i indirin.'
        : 'Katalog PDF yüklenemedi. Lütfen sayfayı yenileyin veya PDF’i indirin.'
    );
    return;
  }

  if (!images?.length) {
    overlay.fail('Katalogda sayfa bulunamadı. PDF’i indirerek inceleyebilirsiniz.');
    return;
  }

  const { w, h } = await measureImage(images[0]);
  const aspect = w / h;
  const baseWidth = 420;
  const baseHeight = Math.round(baseWidth / aspect);

  const pageFlip = new St.PageFlip(document.getElementById('book'), {
    width: baseWidth,
    height: baseHeight,
    size: 'stretch',
    minWidth: 240,
    maxWidth: 640,
    minHeight: 340,
    maxHeight: 900,
    maxShadowOpacity: 0.6,
    showCover: true,
    mobileScrollSupport: false,
    usePortrait: true,
    flippingTime: 800,
    useMouseEvents: true,
  });

  pageFlip.loadFromImages(images);
  applyStuccoBackground(pageFlip);
  window.flipbookInstance = pageFlip; // handy for console debugging / custom integrations

  overlay.hide();

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const indicator = document.getElementById('pageIndicator');
  const soundBtn = document.getElementById('soundBtn');
  const fsBtn = document.getElementById('fsBtn');
  const hint = document.getElementById('hint');

  function updateIndicator() {
    const total = pageFlip.getPageCount();
    const current = pageFlip.getCurrentPageIndex() + 1;
    indicator.textContent = `${current} / ${total}`;
    prevBtn.disabled = current <= 1;
    nextBtn.disabled = current >= total;
  }

  function dismissHint() {
    if (hint) hint.classList.add('hidden');
  }

  pageFlip.on('flip', () => {
    updateIndicator();
    playFlipSound();
    dismissHint();
  });

  pageFlip.on('init', updateIndicator);

  prevBtn.addEventListener('click', () => { ensureAudio(); pageFlip.flipPrev(); });
  nextBtn.addEventListener('click', () => { ensureAudio(); pageFlip.flipNext(); });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { ensureAudio(); pageFlip.flipNext(); }
    if (e.key === 'ArrowLeft') { ensureAudio(); pageFlip.flipPrev(); }
  });

  soundBtn.addEventListener('click', () => {
    soundOn = !soundOn;
    localStorage.setItem('flipbook-sound', soundOn ? 'on' : 'off');
    soundBtn.classList.toggle('off', !soundOn);
    soundBtn.textContent = soundOn ? '\u{1F50A}' : '\u{1F507}';
    if (soundOn) { ensureAudio(); playFlipSound(); }
  });
  soundBtn.classList.toggle('off', !soundOn);
  soundBtn.textContent = soundOn ? '\u{1F50A}' : '\u{1F507}';

  fsBtn.addEventListener('click', () => {
    const stage = document.querySelector('.flipbook-stage');
    if (!document.fullscreenElement) {
      stage.requestFullscreen?.();
    } else {
      document.exitFullscreen?.();
    }
  });

  document.getElementById('book').addEventListener('mousedown', dismissHint, { once: true });
  document.getElementById('book').addEventListener('touchstart', dismissHint, { once: true });
  // size:'stretch' makes the library track window resizes on its own.
});
