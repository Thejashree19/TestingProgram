from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ---------------------------------------
# 1. Open Browser
# ---------------------------------------

driver = webdriver.Chrome()

driver.maximize_window()


try:

    # ---------------------------------------
    # 2. Open Website
    # ---------------------------------------

    driver.get(
        "https://the-internet.herokuapp.com/javascript_alerts"
    )

    time.sleep(2)

    # =======================================
    # ALERT
    # =======================================

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Alert']"
    ).click()

    alert = driver.switch_to.alert

    print("Alert Text:", alert.text)

    alert.accept()

    print("Alert accepted")


    # =======================================
    # CONFIRMATION ALERT
    # =======================================

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Confirm']"
    ).click()

    alert = driver.switch_to.alert

    print("Confirm Text:", alert.text)

    alert.dismiss()

    print("Confirmation dismissed")


    # =======================================
    # PROMPT ALERT
    # =======================================

    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Prompt']"
    ).click()

    alert = driver.switch_to.alert

    print("Prompt Text:", alert.text)

    alert.send_keys("Thejashree")

    alert.accept()

    print("Prompt accepted")


    time.sleep(2)


except Exception as e:

    print("Error:", e)


finally:

    driver.quit()

    print("Browser closed")