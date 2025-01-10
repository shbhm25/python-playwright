import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # emailtxtbox = page.wait_for_selector('#email')
    # emailtxtbox.type('test@gmail.com')
    # buttonogin = page.wait_for_selector('#enterimg')
    # buttonogin.click()



    username = page.wait_for_selector('input[name = "username"]')
    username.type('Admin')
    password = page.wait_for_selector('input[name = "password"]')
    password.type('admin123')
    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3)