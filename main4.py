from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# ---------------------------------------
# 1. Open Chrome
# ---------------------------------------

driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()


# ---------------------------------------
# 2. Open Website
# ---------------------------------------

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(2)


# ---------------------------------------
# 3. Print Title and URL
# ---------------------------------------

print("Title:", driver.title)

print("URL:", driver.current_url)


# ---------------------------------------
# 4. Enter Text
# ---------------------------------------

text_box = driver.find_element(By.NAME, "my-text")

if text_box.is_displayed() and text_box.is_enabled():

    text_box.send_keys("Thejashree")

    print("Text entered successfully")


# ---------------------------------------
# 5. Enter Password
# ---------------------------------------

password = driver.find_element(By.NAME, "my-password")

password.send_keys("Test@123")


# ---------------------------------------
# 6. Enter Text Area
# ---------------------------------------

text_area = driver.find_element(By.NAME, "my-textarea")

text_area.send_keys("This is Selenium Python automation practice.")


# ---------------------------------------
# 7. Checkbox
# ---------------------------------------

checkbox = driver.find_element(By.ID, "my-check-1")

if not checkbox.is_selected():

    checkbox.click()

    print("Checkbox selected")


# ---------------------------------------
# 8. Radio Button
# ---------------------------------------

radio = driver.find_element(By.ID, "my-radio-1")

if not radio.is_selected():

    radio.click()

    print("Radio button selected")


# ---------------------------------------
# 9. Dropdown
# ---------------------------------------

dropdown = driver.find_element(By.NAME, "my-select")

select = Select(dropdown)

select.select_by_visible_text("Two")

print("Dropdown selected")


# ---------------------------------------
# 10. Submit
# ---------------------------------------

submit = driver.find_element(By.TAG_NAME, "button")

if submit.is_enabled():

    submit.click()

    print("Form submitted successfully")


# ---------------------------------------
# 11. Wait
# ---------------------------------------

time.sleep(2)


# ---------------------------------------
# 12. Print final information
# ---------------------------------------

print("Final Title:", driver.title)

print("Final URL:", driver.current_url)


# ---------------------------------------
# 13. Close Browser
# ---------------------------------------

driver.quit()