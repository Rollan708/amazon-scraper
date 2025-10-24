# Minimal realistic Playwright scraper demo (works as example)
from playwright.sync_api import sync_playwright
import csv

def scrape_sample():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")  # demo target
        title = page.title()
        # Demo extracted fields
        rows = [{"title": title, "price": "N/A", "rating": "N/A"}]
        with open("amazon_demo.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
            writer.writeheader()
            writer.writerows(rows)
        browser.close()

if __name__ == "__main__":
    scrape_sample()
