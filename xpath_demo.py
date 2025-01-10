from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector('//input[@name = "username"]')
    username.click()
    password = page.wait_for_selector('//input[@name = "password"]')
    password.click()
    login_button = page.wait_for_selector('//button[@type="submit"]')
    login_button.click()
