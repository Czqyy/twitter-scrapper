from playwright.sync_api import sync_playwright, Playwright
from dotenv import load_dotenv
import os

load_dotenv() 

def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch()
    login(browser.new_page())
    

def login(page):
    """
    Navigate to Twitter login page and login using user credentials
    """
    page.goto("https://x.com/i/flow/login")
    page.wait_for_timeout(3000)
    page.screenshot(path='screenshots/login_page.png')

    page.locator('input[autocomplete="username"]').fill(os.environ['email'])
    page.screenshot(path='screenshots/filled_details.png')

    page.get_by_role('button', name='Next').click()
    page.wait_for_timeout(3000)
    page.locator('input[type="password"]').fill(os.environ['password'])
    page.get_by_test_id('LoginForm_Login_Button').click()       # Log in button happens to have data-testid attribute
    page.wait_for_timeout(3000)
    page.screenshot(path='screenshots/homepage.png')


def searchPost(page, post):
    """
    
    """
    pass

with sync_playwright() as playwright:
    run(playwright)
