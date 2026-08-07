from selenium import webdriver
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the website
driver.get("https://www.google.com")

# Wait for 3 seconds
time.sleep(3)

# Print the page title
print("Page Title :", driver.title)

# Print the current URL
print("Current URL :", driver.current_url)

# Print the length of page source
print("Page Source Length :", len(driver.page_source))

# Close the browser
driver.quit()