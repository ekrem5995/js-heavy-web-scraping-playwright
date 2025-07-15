
import csv
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Load listing URLs from existing CSV
links = []
with open("notebook - notebook.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        links.append(row["Link"])

print(f"Loaded {len(links)} listing links.")

# Step 2: Setup undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

# Step 3: Visit each listing and extract detail info
detailed_data = []
for i, url in enumerate(links[:20]):  # LIMIT to first 20 for testing
    print(f"Scraping detail page {i+1}: {url}")
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "classifiedTitle"))
        )
        time.sleep(1)

        # Title
        title = driver.find_element(By.ID, "classifiedTitle").text.strip()

        # Description
        try:
            desc = driver.find_element(By.ID, "classifiedDescription").text.strip()
        except:
            desc = ""

        # Location (usually under map)
        try:
            loc = driver.find_element(By.CSS_SELECTOR, ".classifiedInfo .classified-location").text.strip()
        except:
            loc = ""

        # Seller info
        try:
            seller = driver.find_element(By.CSS_SELECTOR, ".userNameTop").text.strip()
        except:
            seller = "Bireysel"

        # First image
        try:
            img = driver.find_element(By.CSS_SELECTOR, "#classifiedDetail .classifiedDetail .showcase .left img").get_attribute("src")
        except:
            img = ""

        detailed_data.append([title, desc, loc, seller, img, url])
        time.sleep(1)

    except Exception as e:
        print("Error:", e)
        continue

driver.quit()

# Step 4: Save details
with open("notebook_detailed.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Description", "Location", "Seller", "Image", "URL"])
    writer.writerows(detailed_data)

print("Saved notebook_detailed.csv")
