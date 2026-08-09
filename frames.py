from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ---------------------------------------
# 1. Open Chrome
# ---------------------------------------

driver = webdriver.Chrome()

driver.maximize_window()


try:

    # ---------------------------------------
    # 2. Open Website
    # ---------------------------------------

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

    print("Website opened")

    # ---------------------------------------
    # 3. Create Explicit Wait
    # ---------------------------------------

    wait = WebDriverWait(driver, 10)

    # ---------------------------------------
    # 4. Click Add Button
    # ---------------------------------------

    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "adder")
        )
    )

    add_button.click()

    print("Add button clicked")

    # ---------------------------------------
    # 5. Wait for Dynamic Element
    # ---------------------------------------

    dynamic_element = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "box0")
        )
    )

    # ---------------------------------------
    # 6. Check Element
    # ---------------------------------------

    if dynamic_element.is_displayed():

        print("Dynamic element is displayed")

    else:

        print("Dynamic element is not displayed")


except Exception as e:

    print("Test failed")

    print("Error:", e)


finally:

    # ---------------------------------------
    # 7. Close Browser
    # ---------------------------------------

    driver.quit()

    print("Browser closed")