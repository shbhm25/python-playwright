from cProfile import label
from select import select

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    # select_dropdown = page.query_selector('//select[@id="Skills"]')
    # select_dropdown.select_option(label = 'Art Design')
    page.wait_for_timeout(5000)

    page.select_option('//select[@id="Skills"]',label='Art Design')