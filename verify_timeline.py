from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("http://localhost:8080/demystifying-english-tenses-timeline-guide.html", wait_until="networkidle")
    page.screenshot(path="verification_timeline_desktop.png", full_page=False)

    # Mobile view
    mobile_page = browser.new_page(viewport={"width": 390, "height": 844})
    mobile_page.goto("http://localhost:8080/demystifying-english-tenses-timeline-guide.html", wait_until="networkidle")
    mobile_page.screenshot(path="verification_timeline_mobile.png", full_page=False)

    browser.close()

print("Captured screenshots successfully.")
