import re

with open('scratch/original_utf8.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CV button in Navbar
old_nav_actions = '''      <button id="themeToggle" aria-label="Toggle Light/Dark Theme"
        style="background:none; border:none; color: var(--primary-color); font-size:1.2rem; cursor:pointer;">
        <i class="fas fa-sun"></i>
      </button>'''

new_nav_actions = '''      <div style="display:flex; align-items:center; gap:1.2rem;">
        <a href="https://drive.google.com/uc?export=download&id=1vdANAd1qYYED46vdsptvZv6XiwpUfCDp" target="_blank" rel="noopener noreferrer" class="btn-cv-nav" title="Download Resume CV">
          <i class="fas fa-file-arrow-down"></i> Resume CV
        </a>
        <button id="themeToggle" aria-label="Toggle Light/Dark Theme"
          style="background:none; border:none; color: var(--primary-color); font-size:1.2rem; cursor:pointer;">
          <i class="fas fa-sun"></i>
        </button>
      </div>'''

text = text.replace(old_nav_actions, new_nav_actions)

# 2. Add btn-cv-nav CSS
cv_css = '''
    .btn-cv-nav {
      background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
      color: #000;
      padding: 0.5rem 1.25rem;
      border-radius: 30px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.3s ease;
      box-shadow: 0 0 15px rgba(0, 245, 255, 0.3);
    }
    .btn-cv-nav:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 25px rgba(255, 107, 107, 0.5);
      color: #000;
    }
'''

text = text.replace('/* Custom Scrollbar */', cv_css + '\n    /* Custom Scrollbar */')

# 3. Update social links in hero and footer
old_hero_socials = '''    <div class="social-links">
      <a href="https://github.com/HasinduBimsara" aria-label="GitHub" target="_blank" rel="noopener">
        <i class="fab fa-github"></i>
      </a>
      <a href="https://www.linkedin.com/in/hasindu-bimsara" aria-label="LinkedIn" target="_blank" rel="noopener">
        <i class="fab fa-linkedin-in"></i>
      </a>
      <a href="mailto:bimsarapremarathna@gmail.com" aria-label="Gmail">
        <i class="fas fa-envelope"></i>
      </a>
    </div>'''

new_hero_socials = '''    <div class="social-links">
      <a href="https://github.com/HasinduBimsara" aria-label="GitHub" target="_blank" rel="noopener" title="GitHub">
        <i class="fab fa-github"></i>
      </a>
      <a href="https://www.linkedin.com/in/hasindubimsara/" aria-label="LinkedIn" target="_blank" rel="noopener" title="LinkedIn">
        <i class="fab fa-linkedin-in"></i>
      </a>
      <a href="https://medium.com/" aria-label="Medium" target="_blank" rel="noopener" title="Medium">
        <i class="fab fa-medium-m"></i>
      </a>
      <a href="https://www.instagram.com/bimxara_22._/" aria-label="Instagram" target="_blank" rel="noopener" title="Instagram">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="mailto:bimsarapremarathna123@gmail.com" aria-label="Email" title="Email">
        <i class="fas fa-envelope"></i>
      </a>
      <a href="https://x.com/hasindubimsaraX" aria-label="Twitter" target="_blank" rel="noopener" title="Twitter / X">
        <i class="fab fa-twitter"></i>
      </a>
    </div>'''

text = text.replace(old_hero_socials, new_hero_socials)

# Update footer socials
old_footer_socials = '''      <div class="follow-me-icons">
        <a href="https://github.com/HasinduBimsara" aria-label="GitHub" target="_blank" rel="noopener">
          <i class="fab fa-github"></i>
        </a>
        <a href="https://www.linkedin.com/in/hasindubimsara/" aria-label="LinkedIn" target="_blank" rel="noopener">
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="https://x.com/hasindubimsaraX" aria-label="Twitter" target="_blank" rel="noopener">
          <i class="fab fa-twitter"></i>
        </a>
        <a href="https://www.facebook.com/Mr.HasinduBimsara" aria-label="Facebook" target="_blank" rel="noopener">
          <i class="fab fa-facebook-f"></i>
        </a>
        <a href="https://instagram.com/hasindu_bimsara_" aria-label="Instagram" target="_blank" rel="noopener">
          <i class="fab fa-instagram"></i>
        </a>
        <button id="backToTop" aria-label="Back to Top" title="Back to Top">
          <i class="fas fa-arrow-up"></i>
        </button>
      </div>'''

new_footer_socials = '''      <div class="follow-me-icons">
        <a href="https://github.com/HasinduBimsara" aria-label="GitHub" target="_blank" rel="noopener" title="GitHub">
          <i class="fab fa-github"></i>
        </a>
        <a href="https://www.linkedin.com/in/hasindubimsara/" aria-label="LinkedIn" target="_blank" rel="noopener" title="LinkedIn">
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="https://medium.com/" aria-label="Medium" target="_blank" rel="noopener" title="Medium">
          <i class="fab fa-medium-m"></i>
        </a>
        <a href="https://www.instagram.com/bimxara_22._/" aria-label="Instagram" target="_blank" rel="noopener" title="Instagram">
          <i class="fab fa-instagram"></i>
        </a>
        <a href="mailto:bimsarapremarathna123@gmail.com" aria-label="Email" title="Email">
          <i class="fas fa-envelope"></i>
        </a>
        <a href="https://x.com/hasindubimsaraX" aria-label="Twitter" target="_blank" rel="noopener" title="Twitter / X">
          <i class="fab fa-twitter"></i>
        </a>
        <button id="backToTop" aria-label="Back to Top" title="Back to Top">
          <i class="fas fa-arrow-up"></i>
        </button>
      </div>'''

text = text.replace(old_footer_socials, new_footer_socials)

# Update copyright year to 2026
text = text.replace('© 2025 Hasindu Bimsara. All rights reserved.', '© 2026 Hasindu Bimsara. All rights reserved.')
text = text.replace('bimsarapremarathna123gmail.com', 'bimsarapremarathna123@gmail.com')

# 4. Add cyber neon preloader
preloader_html = '''
  <!-- Sleek Cyber Preloader -->
  <div id="site-preloader" style="position:fixed; top:0; left:0; width:100%; height:100%; background:#000000; z-index:99999; display:flex; flex-direction:column; justify-content:center; align-items:center; transition:opacity 0.6s ease, visibility 0.6s ease;">
    <div style="font-size:1.8rem; font-weight:800; background:linear-gradient(45deg, var(--primary-color), var(--accent-color)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:1.2rem; letter-spacing:1px;">
      HASINDU BIMSARA
    </div>
    <div style="width:240px; height:4px; background:rgba(255,255,255,0.1); border-radius:4px; overflow:hidden; margin-bottom:0.8rem;">
      <div id="preloader-bar" style="width:0%; height:100%; background:linear-gradient(90deg, var(--primary-color), var(--accent-color)); transition:width 0.1s linear;"></div>
    </div>
    <div id="preloader-pct" style="color:var(--primary-color); font-family:monospace; font-size:0.95rem; font-weight:600;">0%</div>
  </div>
'''

preloader_js = '''
      // Cyber Preloader
      const sitePreloader = document.getElementById("site-preloader");
      const preloaderBar = document.getElementById("preloader-bar");
      const preloaderPct = document.getElementById("preloader-pct");
      if (sitePreloader && preloaderBar && preloaderPct) {
        let p = 0;
        const interval = setInterval(() => {
          p += Math.floor(Math.random() * 15) + 5;
          if (p >= 100) {
            p = 100;
            clearInterval(interval);
            preloaderBar.style.width = "100%";
            preloaderPct.textContent = "100%";
            setTimeout(() => {
              sitePreloader.style.opacity = "0";
              sitePreloader.style.visibility = "hidden";
            }, 300);
          } else {
            preloaderBar.style.width = p + "%";
            preloaderPct.textContent = p + "%";
          }
        }, 40);
      }
'''

text = text.replace('<body>', '<body>\n' + preloader_html)
text = text.replace('document.addEventListener("DOMContentLoaded", () => {', 'document.addEventListener("DOMContentLoaded", () => {\n' + preloader_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: index.html has been updated with the original color theme, structure, and all requested enhancements!")
