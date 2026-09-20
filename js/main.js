(() => {
  const root = document.documentElement.dataset.root || "";

  /* Mobile nav */
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  if (toggle && nav) {
    const setNavOpen = (open) => {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    };
    const closeNav = () => setNavOpen(false);

    toggle.addEventListener("click", () => {
      setNavOpen(!nav.classList.contains("is-open"));
    });
    nav.querySelectorAll("button.nav-parent").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (window.matchMedia("(max-width: 820px)").matches) {
          btn.parentElement.classList.toggle("is-open");
        }
      });
    });
    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        if (window.matchMedia("(max-width: 820px)").matches) closeNav();
      });
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) closeNav();
    });
    window.matchMedia("(max-width: 820px)").addEventListener("change", (e) => {
      if (!e.matches) closeNav();
    });
  }

  /* Hero slider */
  const slider = document.querySelector(".hero-slider");
  if (slider) {
    const slides = [...slider.querySelectorAll(".slide")];
    const dotsWrap = slider.querySelector(".slider-dots");
    const prev = slider.querySelector("[data-prev]");
    const next = slider.querySelector("[data-next]");
    let i = 0;
    let timer;

    slides.forEach((_, idx) => {
      const b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", `Slayt ${idx + 1}`);
      if (idx === 0) b.classList.add("is-active");
      b.addEventListener("click", () => go(idx));
      dotsWrap?.appendChild(b);
    });
    const dots = [...(dotsWrap?.querySelectorAll("button") || [])];

    const go = (n) => {
      slides[i].classList.remove("is-active");
      dots[i]?.classList.remove("is-active");
      i = (n + slides.length) % slides.length;
      slides[i].classList.add("is-active");
      dots[i]?.classList.add("is-active");
      restart();
    };
    const restart = () => {
      clearInterval(timer);
      timer = setInterval(() => go(i + 1), 5500);
    };
    prev?.addEventListener("click", () => go(i - 1));
    next?.addEventListener("click", () => go(i + 1));
    slider.addEventListener("mouseenter", () => clearInterval(timer));
    slider.addEventListener("mouseleave", restart);
    restart();
  }

  /* Reveal */
  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -30px 0px" }
    );
    els.forEach((el) => io.observe(el));
  } else {
    els.forEach((el) => el.classList.add("in"));
  }

  /* Year */
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  /* Shared lightbox for catalog galleries */
  const lightbox = (() => {
    let lb = document.querySelector(".lightbox");
    if (!lb) {
      lb = document.createElement("div");
      lb.className = "lightbox";
      lb.setAttribute("role", "dialog");
      lb.setAttribute("aria-modal", "true");
      lb.setAttribute("aria-label", "Görsel önizleme");
      lb.innerHTML = `
        <button type="button" class="lightbox__close" aria-label="Kapat">×</button>
        <button type="button" class="lightbox__nav lightbox__nav--prev" aria-label="Önceki görsel">‹</button>
        <button type="button" class="lightbox__nav lightbox__nav--next" aria-label="Sonraki görsel">›</button>
        <figure class="lightbox__figure">
          <img class="lightbox__img" alt="" draggable="false" />
          <figcaption class="lightbox__caption"></figcaption>
        </figure>`;
      document.body.appendChild(lb);
    }

    let active = null;
    let touchX = 0;
    let touchY = 0;
    let swiping = false;

    const img = lb.querySelector(".lightbox__img");
    const caption = lb.querySelector(".lightbox__caption");
    const isOpen = () => lb.classList.contains("is-open");

    const sync = () => {
      if (!active || !isOpen()) return;
      const item = active.getItem();
      if (!item) return;
      img.src = item.src;
      img.alt = item.alt || "";
      caption.textContent = [item.code, item.label, item.count]
        .filter(Boolean)
        .join(" · ");
    };

    const close = () => {
      lb.classList.remove("is-open");
      document.body.style.overflow = "";
      active = null;
    };

    const open = (controller) => {
      active = controller;
      lb.classList.add("is-open");
      document.body.style.overflow = "hidden";
      sync();
    };

    lb.querySelector(".lightbox__close").addEventListener("click", close);
    lb.querySelector(".lightbox__nav--prev").addEventListener("click", (e) => {
      e.stopPropagation();
      active?.prev();
      sync();
    });
    lb.querySelector(".lightbox__nav--next").addEventListener("click", (e) => {
      e.stopPropagation();
      active?.next();
      sync();
    });
    lb.addEventListener("click", (e) => {
      if (e.target === lb) close();
    });

    document.addEventListener("keydown", (e) => {
      if (!isOpen()) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        active?.prev();
        sync();
      }
      if (e.key === "ArrowRight") {
        e.preventDefault();
        active?.next();
        sync();
      }
    });

    const onTouchStart = (e) => {
      if (!isOpen() || e.touches.length !== 1) return;
      touchX = e.touches[0].clientX;
      touchY = e.touches[0].clientY;
      swiping = true;
    };
    const onTouchMove = (e) => {
      if (!swiping) return;
      const dx = e.touches[0].clientX - touchX;
      const dy = e.touches[0].clientY - touchY;
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 12) e.preventDefault();
    };
    const onTouchEnd = (e) => {
      if (!swiping) return;
      swiping = false;
      const t = e.changedTouches[0];
      const dx = t.clientX - touchX;
      const dy = t.clientY - touchY;
      if (Math.abs(dx) < 48 || Math.abs(dx) < Math.abs(dy)) return;
      if (dx < 0) active?.next();
      else active?.prev();
      sync();
    };

    lb.addEventListener("touchstart", onTouchStart, { passive: true });
    lb.addEventListener("touchmove", onTouchMove, { passive: false });
    lb.addEventListener("touchend", onTouchEnd, { passive: true });

    return { open, close, sync, isOpen };
  })();

  /* Catalog viewer (stage + thumbs) */
  document.querySelectorAll("[data-catalog]").forEach((root) => {
    const stageImg = root.querySelector("[data-catalog-stage]");
    const stageCode = root.querySelector("[data-catalog-code]");
    const stageLabel = root.querySelector("[data-catalog-label]");
    const stageCount = root.querySelector("[data-catalog-count]");
    const thumbs = [...root.querySelectorAll("[data-catalog-thumb]")];
    const prev = root.querySelector("[data-catalog-prev]");
    const next = root.querySelector("[data-catalog-next]");
    if (!stageImg || !thumbs.length) return;

    let i = Math.max(0, thumbs.findIndex((t) => t.classList.contains("is-active")));
    if (i < 0) i = 0;

    const show = (idx) => {
      i = (idx + thumbs.length) % thumbs.length;
      const t = thumbs[i];
      const src = t.getAttribute("data-src") || t.querySelector("img")?.src;
      const code = t.getAttribute("data-code") || "";
      const label = t.getAttribute("data-label") || "";
      const alt = t.querySelector("img")?.alt || code;
      stageImg.src = src;
      stageImg.alt = alt;
      if (stageCode) stageCode.textContent = code;
      if (stageLabel) stageLabel.textContent = label;
      if (stageCount) {
        stageCount.innerHTML = `<b>${String(i + 1).padStart(2, "0")}</b> / ${String(thumbs.length).padStart(2, "0")}`;
      }
      thumbs.forEach((el, n) => el.classList.toggle("is-active", n === i));
      t.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
      if (lightbox.isOpen()) lightbox.sync();
    };

    const controller = {
      prev: () => show(i - 1),
      next: () => show(i + 1),
      getItem: () => {
        const t = thumbs[i];
        return {
          src: t.getAttribute("data-src") || t.querySelector("img")?.src,
          alt: stageImg.alt || t.getAttribute("data-code") || "",
          code: t.getAttribute("data-code") || "",
          label: t.getAttribute("data-label") || "",
          count: `${String(i + 1).padStart(2, "0")} / ${String(thumbs.length).padStart(2, "0")}`,
        };
      },
    };

    thumbs.forEach((t, idx) => t.addEventListener("click", () => show(idx)));
    prev?.addEventListener("click", () => show(i - 1));
    next?.addEventListener("click", () => show(i + 1));
    /* Stage swipe (mobile) also advances gallery without opening lightbox */
    let sx = 0;
    let sy = 0;
    let stageSwipe = false;
    let didSwipe = false;
    const stageBtn = root.querySelector("[data-catalog-zoom]");
    stageBtn?.addEventListener(
      "touchstart",
      (e) => {
        if (e.touches.length !== 1) return;
        sx = e.touches[0].clientX;
        sy = e.touches[0].clientY;
        stageSwipe = true;
        didSwipe = false;
      },
      { passive: true }
    );
    stageBtn?.addEventListener(
      "touchend",
      (e) => {
        if (!stageSwipe) return;
        stageSwipe = false;
        const t = e.changedTouches[0];
        const dx = t.clientX - sx;
        const dy = t.clientY - sy;
        if (Math.abs(dx) < 48 || Math.abs(dx) < Math.abs(dy)) return;
        didSwipe = true;
        e.preventDefault();
        if (dx < 0) show(i + 1);
        else show(i - 1);
      },
      { passive: false }
    );

    stageBtn?.addEventListener("click", (e) => {
      if (didSwipe) {
        e.preventDefault();
        e.stopImmediatePropagation();
        didSwipe = false;
        return;
      }
      lightbox.open(controller);
    });

    document.addEventListener("keydown", (e) => {
      if (lightbox.isOpen()) return;
      if (!root.offsetParent) return;
      if (e.key === "ArrowLeft") show(i - 1);
      if (e.key === "ArrowRight") show(i + 1);
    });
    show(i);
  });

  /* Product image zoom: mobilya + laminant parke + rehber galleries */
  (() => {
    if (!document.querySelector(".mobilya-gallery, .mobilya-side, .parke-gallery, .parke-side, .rehber-gallery")) return;

    const items = [];
    const frames = [];

    const pushImg = (img, frame) => {
      if (!img?.src) return;
      const idx = items.length;
      items.push({
        src: img.currentSrc || img.src,
        alt: img.alt || "",
        label: img.alt || "",
        count: "",
      });
      frames.push({ frame, img, idx });
      frame.setAttribute("role", "button");
      frame.setAttribute("tabindex", "0");
      frame.setAttribute("aria-label", "Görseli büyüt");
    };

    document
      .querySelectorAll(
        ".mobilya-gallery figure, .parke-gallery figure, .rehber-gallery figure, .mobilya-side, .parke-side"
      )
      .forEach((fig) => {
        const img = fig.querySelector("img");
        if (img) pushImg(img, fig);
      });
    if (!items.length) return;

    items.forEach((it, n) => {
      it.count = `${String(n + 1).padStart(2, "0")} / ${String(items.length).padStart(2, "0")}`;
    });

    let i = 0;
    const controller = {
      prev: () => {
        i = (i - 1 + items.length) % items.length;
      },
      next: () => {
        i = (i + 1) % items.length;
      },
      getItem: () => items[i],
    };

    const openAt = (idx) => {
      i = idx;
      lightbox.open(controller);
    };

    const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");

    frames.forEach(({ frame, img, idx }) => {
      frame.addEventListener("click", () => openAt(idx));
      frame.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openAt(idx);
        }
      });

      if (!finePointer.matches) return;

      frame.addEventListener("mousemove", (e) => {
        const r = frame.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        frame.classList.add("is-hover");
        img.style.transform = `scale(1.14) translate(${px * -8}%, ${py * -8}%)`;
      });
      frame.addEventListener("mouseleave", () => {
        frame.classList.remove("is-hover");
        img.style.transform = "";
      });
    });
  })();

  /* WhatsApp: floating button sitewide + contact form → wa.me */
  const WA_PHONE = "905422362365";
  const waUrl = (text) =>
    `https://wa.me/${WA_PHONE}?text=${encodeURIComponent(text)}`;

  if (!document.querySelector(".wa-float")) {
    const a = document.createElement("a");
    a.className = "wa-float";
    a.href = waUrl(
      "Merhaba, eminkapiosmaniye.com üzerinden yazıyorum. Bilgi almak istiyorum."
    );
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.setAttribute("aria-label", "WhatsApp ile yazın");
    a.innerHTML = `<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M17.47 14.38c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.95 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.05 1.02-1.05 2.5s1.07 2.9 1.22 3.1c.15.2 2.11 3.22 5.11 4.51.71.31 1.27.49 1.7.63.72.23 1.37.2 1.89.12.58-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35z"/><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.95.57 3.76 1.56 5.3L2 22l4.93-1.63a9.86 9.86 0 0 0 5.11 1.41h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15h-.01a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.09 1.02 1.04-3.01-.2-.31a8.2 8.2 0 0 1-1.26-4.4c0-4.54 3.7-8.23 8.24-8.23 4.54 0 8.23 3.7 8.23 8.23 0 4.54-3.7 8.23-8.23 8.23z"/></svg><span>WhatsApp</span>`;
    document.body.appendChild(a);
  }

  const contactForm = document.getElementById("contact-wa-form");
  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const fd = new FormData(contactForm);
      const ad = String(fd.get("ad") || "").trim();
      const telefon = String(fd.get("telefon") || "").trim();
      const konu = String(fd.get("konu") || "").trim();
      const mesaj = String(fd.get("mesaj") || "").trim();
      const phone = contactForm.getAttribute("data-wa-phone") || WA_PHONE;
      const body = [
        "📋 *Emin Kapı — Web sitesi iletişim formu*",
        "",
        `👤 Ad: ${ad}`,
        `📞 Telefon: ${telefon}`,
        `📌 Konu: ${konu}`,
        mesaj ? `💬 Mesaj: ${mesaj}` : "",
        "",
        "—",
        "_Bu mesaj eminkapiosmaniye.com iletişim formundan gönderildi._",
      ]
        .filter((line) => line !== "")
        .join("\n");
      window.open(
        `https://wa.me/${phone}?text=${encodeURIComponent(body)}`,
        "_blank",
        "noopener,noreferrer"
      );
    });
  }
})();
