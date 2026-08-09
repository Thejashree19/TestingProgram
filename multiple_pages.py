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
    # 2. Open Parent Website
    # ---------------------------------------

    driver.get("https://www.google.com")

    print("Parent Title:", driver.title)

    # ---------------------------------------
    # 3. Store Parent Window
    # ---------------------------------------

    parent_window = driver.current_window_handle

    print("Parent Window:", parent_window)

    # ---------------------------------------
    # 4. Open New Tab
    # ---------------------------------------

    driver.switch_to.new_window("tab")

    # ---------------------------------------
    # 5. Open Selenium Website
    # ---------------------------------------

    driver.get("https://www.selenium.dev")

    time.sleep(2)

    print("New Tab Title:", driver.title)

    # ---------------------------------------
    # 6. Get All Windows
    # ---------------------------------------

    windows = driver.window_handles

    print("Number of Windows/Tabs:", len(windows))

    # ---------------------------------------
    # 7. Switch Through Windows
    # ---------------------------------------

    for window in windows:

        driver.switch_to.window(window)

        print(
            "Window:",
            window,
            "Title:",
            driver.title
        )

    # ---------------------------------------
    # 8. Return to Parent
    # ---------------------------------------

    driver.switch_to.window(parent_window)

    print("Returned to Parent")

    print(
        "Parent Title:",
        driver.title
    )

    time.sleep(2)


except Exception as e:

    print("Error:", e)


finally:

    driver.quit()

    print("Browser closed")