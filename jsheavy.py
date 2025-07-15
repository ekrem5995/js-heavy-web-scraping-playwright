from playwright.sync_api import sync_playwright #Playwright's synchronous (easy) interface.
import csv

data = []  # List to store extracted data

with sync_playwright() as p: #Starts the Playwright engine. p is your browser controller.Everything inside this with block runs Playwright commands.
    browser = p.chromium.launch(headless=False)#headless=False means you see the browser window open. You can change it to True when deploying.
    page = browser.new_page()
    page.goto("https://www.sahibinden.com/bilgisayar-dizustu-notebook")
    page.wait_for_timeout(5000)  #JS render

    listings = page.query_selector_all(".searchResultsItem")#Finds all elements (divs or rows) on the page that represent a listing.

    for item in listings:#Loop through each individual listing and extract its info.
        title_element = item.query_selector("a")#Finds: a: The link tag containing the title and link
        price_element = item.query_selector(".searchResultsPriceValue")#Finds .searchResultsPriceValue: The price of the listing

        if title_element and price_element: #Ensures the elements were found (not None) avoids errors if something is missing.
            title = title_element.inner_text().strip()#extracts Title text of the listing
            link = title_element.get_attribute("href")#extracts Link URL
            price = price_element.inner_text().strip()#extracts Price text .strip() removes extra spaces or line breaks.

            full_link = f"https://www.sahibinden.com{link}"

            print(f"{title} - {price} - {full_link}")

            data.append({
                "title": title,   #
                "price": price,   #Adds the extracted data to the data list for later export.
                "link": full_link #
            })

    browser.close()

# Export to CSV
with open("notebook.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    for item in data:
        writer.writerow([item['title'], item['price'], item['link']])

