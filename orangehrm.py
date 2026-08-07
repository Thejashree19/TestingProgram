from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os

# ---------------- LOGGING ----------------
logging.basicConfig(
    filename="selenium.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program Started")

# Create Screenshot folder
if not os.path.exists("Screenshots"):
    os.makedirs("Screenshots")

# Launch Browser
driver = webdriver.Chrome()

try:
    driver.maximize_window()

    # ---------------- OPEN WEBSITE ----------------
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    print("Website Opened")
    logging.info("Website Opened")

    # ---------------- EXPLICIT WAIT ----------------
    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # ---------------- LOGIN ----------------
    username.send_keys("Admin")

    driver.find_element(By.NAME, "password").send_keys("admin123")

    # CSS Selector
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    print("Login Button Clicked")

    # Wait until Dashboard appears
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h6[text()='Dashboard']")
        )
    )

    # ---------------- ASSERTION ----------------
    assert "dashboard" in driver.current_url.lower()

    print("Login Successful")
    logging.info("Login Successful")

    # ---------------- REFRESH ----------------
    driver.refresh()

    print("Page Refreshed")

    # ---------------- NAVIGATION ----------------
    driver.back()

    time.sleep(2)

    driver.forward()

    time.sleep(2)

    # ---------------- JAVASCRIPT EXECUTOR ----------------
    driver.execute_script("window.scrollTo(0,500);")

    time.sleep(2)

    driver.execute_script("window.scrollTo(0,0);")

    # ---------------- SCREENSHOT ----------------
    driver.save_screenshot("Screenshots/dashboard.png")

    print("Screenshot Saved")

    # ---------------- IF CONDITION ----------------
    if "dashboard" in driver.current_url.lower():
        print("Dashboard Loaded")
    else:
        print("Dashboard Not Loaded")

    # ---------------- PAGE TITLE ----------------
    print("Title :", driver.title)

    # ---------------- URL ----------------
    print("URL :", driver.current_url)

    logging.info("Program Executed Successfully")

except Exception as e:

    print("Error :", e)

    logging.error(e)

finally:

    time.sleep(3)

    driver.quit()

    logging.info("Browser Closed")