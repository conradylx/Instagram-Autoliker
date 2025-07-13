import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv


def main():
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    url = "https://www.instagram.com"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    driver.get(url)
    driver.maximize_window()

    try:
        time.sleep(5)
        accept_cookies(driver)
        login(driver, username, password)
        time.sleep(5)
        for _ in range(15):
            like_posts(driver)
        driver.close()
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()


def accept_cookies(driver):
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Allow all cookies')]")
            )
        )
        cookies_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error accepting cookies: {e}")


def login(driver, username, password):
    time.sleep(3)
    username_elem = driver.find_element(By.NAME, "username")
    username_elem.send_keys(username)
    password_elem = driver.find_element(By.NAME, "password")
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.ENTER)


def scroll_and_wait_for_new_posts(driver, timeout=15, check_interval=1):
    old_like_buttons = driver.find_elements(
        By.XPATH,
        '//article//section[1]//div[@role="button"]//svg[contains(@aria-label, "Like") or contains(@aria-label, "Lubię to")]/ancestor::div[@role="button"]',
    )
    old_count = len(old_like_buttons)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(check_interval)
        new_like_buttons = driver.find_elements(
            By.XPATH,
            '//article//section[1]//div[@role="button"]//svg[contains(@aria-label, "Like") or contains(@aria-label, "Lubię to")]/ancestor::div[@role="button"]',
        )
        if len(new_like_buttons) > old_count:
            return True
    return False


def like_posts(driver):
    like_buttons = driver.find_elements(
        By.XPATH, '//article//section[1]//div[@role="button"][1]'
    )
    print(f"Znaleziono {len(like_buttons)} przycisków Like")
    for btn in like_buttons:
        try:
            svg = btn.find_element(By.TAG_NAME, "svg")
            aria_label = svg.get_attribute("aria-label")
            if aria_label in ["Like", "Lubię to"]:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", btn
                )
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
        except Exception as e:
            print(f"Błąd podczas klikania Like: {e}")

    time.sleep(2)


if __name__ == "__main__":
    main()
