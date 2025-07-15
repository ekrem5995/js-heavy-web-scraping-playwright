# 🕷️ Playwright Web Scraping for JavaScript-Heavy Sites

This repository documents my experiments and testing setup for scraping dynamic, JavaScript-heavy websites using **Playwright** and **undetected-chromedriver**. It includes real test cases (e.g., `sahibinden.com`), techniques for bypassing anti-bot measures, and structured data extraction into CSV.

---

## 🧪 Tested Technologies

- ✅ Playwright (JS rendering)  
- ✅ Undetected-Chromedriver (Cloudflare bypass)  
- ✅ Selenium (`WebDriverWait` & `By` locators)  
- ✅ CSV parsing/writing  
- 🔜 Google Sheets or Airtable export  
- 🔜 Random mouse movement + delay behavior for evasion  

---

## 📁 Project Structure

```
playwright-js-scraping/
├── jsheavy4.py         # Main script for detail page scraping
├── notebook.csv             # Input file with URLs
├── README.md
├── .gitignore
└── /screenshots (optional)      # Example output or anti-bot captures
```


## ⚙️ How It Works

1. **Load URLs** from `notebook.csv`  
2. **Launch undetected Chrome** using `undetected_chromedriver`  
3. **Visit each link**, wait for page to fully load (`WebDriverWait`)  
4. **Extract details** (e.g., title, price, features)  
5. **Save results** in structured format (CSV / JSON)

---

## 🚧 Roadmap

- [x] Load links from CSV  
- [x] Extract individual listing details  
- [ ] Add random behavior (scroll, hover, delay) to mimic human use  
- [ ] Parallel browser sessions (multi-threaded scraping)  
- [ ] Headless fallback with stealth mode  
- [ ] Output data to Google Sheets using API  
- [ ] Modularize code (`/utils/`, `/config/`, etc.)

---

## 🛠 Setup

```bash
# Step 1: Install dependenci
# Step 2: Run the script
python jsheavy1-2-3-4.py
```

---

## 🧠 Lessons Learned

- JS-heavy sites like `sahibinden.com` require full browser rendering  
- Cloudflare protections often block traditional scrapers → use `undetected-chromedriver`  
- Always wait for DOM elements explicitly using `WebDriverWait`  
- Mimicking human behavior (scrolling, waiting, random clicks) is essential

---

## 📸 Screenshots

_Example output or UI screenshots go here (if available)._

---

## 📜 License

MIT License – for educational and personal use only.

---

Built by [ekrem5995] as part of scraping + automation mastery.  
Follow the journey. 🚀