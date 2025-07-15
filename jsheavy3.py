import time
import csv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)

# Step 1: Open login page
driver.get("https://secure.sahibinden.com/giris")

# Step 2: Pause for manual login
input("Login manually, then press ENTER to continue...")

# Step 3: Start scraping loop
data = []
for page in range(1, 5):  # You can increase this safely up to 10000+ if needed
    print(f"Scraping Page {page}")
    url = f"https://www.sahibinden.com/bilgisayar-dizustu-notebook?page={page}"
    driver.get(url)

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr[class^='searchResultsItem']"))
        )
    except Exception as e:
        print(f"Skipping page {page} due to error: {e}")
        continue

    rows = driver.find_elements(By.CSS_SELECTOR, "tr[class^='searchResultsItem']")
    print(f"Found {len(rows)} listings on page {page}")

    for row in rows:
        try:
            title_elem = row.find_element(By.CSS_SELECTOR, "td.searchResultsTitleValue a.classifiedTitle")
            price_elem = row.find_element(By.CSS_SELECTOR, "td.searchResultsPriceValue")

            title = title_elem.text.strip()
            price = price_elem.text.strip()
            link = title_elem.get_attribute("href")

            data.append([title, price, link])
        except:
            continue

# Step 4: Save results to CSV
with open("notebook.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    writer.writerows(data)

print(f"Scraped {len(data)} total listings. Data saved to notebook.csv")

# Step 5: Close browser
driver.quit()
