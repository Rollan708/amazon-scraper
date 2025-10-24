from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_amazon():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.amazon.com/s?k=books")
        titles = page.locator("h2 a span").all_text_contents()
        data = [{"title": t} for t in titles[:10]]
        pd.DataFrame(data).to_csv("amazon_data.csv", index=False)
        browser.close()

if __name__ == "__main__":
    scrape_amazon()
