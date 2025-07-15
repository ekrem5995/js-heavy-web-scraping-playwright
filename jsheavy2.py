from playwright.sync_api import sync_playwright
import csv

data = []

with sync_playwright() as p:
    # Launch persistent context with saved user session
    browser = p.chromium.launch_persistent_context(
        user_data_dir="./profile",
        headless=False
    )
    page = browser.new_page()
    page.goto("https://www.sahibinden.com/bilgisayar-dizustu-notebook")

    page.wait_for_timeout(5000)  # Let JavaScript render

    listings = page.query_selector_all(".searchResultsItem")

    for item in listings:
        title_element = item.query_selector("a")
        price_element = item.query_selector(".searchResultsPriceValue")

        if title_element and price_element:
            title = title_element.inner_text().strip()
            link = title_element.get_attribute("href")
            price = price_element.inner_text().strip()

            full_link = f"https://www.sahibinden.com{link}"
            print(f"{title} - {price} - {full_link}")

            data.append({
                "title": title,
                "price": price,
                "link": full_link
            })

    browser.close()

# Export to CSV
with open("notebook.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    for item in data:
        writer.writerow([item['title'], item['price'], item['link']])
