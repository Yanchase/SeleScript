from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def Login(phone, password):

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login_init_by_login"))
    ).click()
    print("Initiated login process.")

    # Click to make sure login fields are ready (if necessary)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login_content_h4"))
    ).click()
    print("Prepared login fields.")

    # Enter the phone number
    phone_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "login_isRegiTele_input"))
    )
    phone_input.send_keys(phone)
    print(f"Entered phone: {phone}")

    # Enter the password
    password_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "login_pwd_input"))
    )
    password_input.send_keys(password)
    print(f"Entered password: {password}")

    # Login button
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login_pwd_submit"))
    ).click()


def buy(buy_time):
    buy_time = datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S.%f")
    while True:
        now = datetime.now()
        if now >= buy_time:
            try:
                WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".select_btn.checkbox.scale_1px.checkbox")
                    )
                ).click()
                WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".go_buy.wd-theme__button1")
                    )
                ).click()
                WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".quick_pay_tips.scale_1px")
                    )
                ).click()

                try:
                    WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, ".clickv-com-vui.v-button__text")
                        )
                    ).click()
                    print("Clicked on popup button.")
                except TimeoutException:
                    print("No popup appeared.")

                break  # Exit the loop if all actions are successful
            except TimeoutException:
                print("Timed out waiting for one of the elements, trying again...")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                break  # Exit loop on unexpected error


# v-com-vui v-button__text

driver_path = "/Users/winwin/Documents/repository/geckodriver/geckodriver"

# Create a new Chrome session using Service
s = Service(driver_path)
driver = webdriver.Firefox(service=s)
driver.implicitly_wait(30)
driver.maximize_window()  # Optional, to maximize the browser window

url = "https://sso.weidian.com/login/index.php?redirect=https%3A%2F%2Fweidian.com%2Fnew-cart%2Findex.php%3Fwfr%3Dc%26ifr%3Ditemdetail%26share_relation%3D45d77cdfd2a55d75_1204884247_1%26spider_token%3D9d15"

driver.get(url)
Login(13215725626, "yan1060732029")
buy("2024-04-20 22:30:00.000000")

# Close the browser window
driver.quit()
