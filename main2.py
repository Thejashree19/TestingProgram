from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open login page
driver.get("https://the-internet.herokuapp.com/login")

# Wait for page to load
time.sleep(2)

# Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click Login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for login
time.sleep(3)

# Print success message
print("Current URL :", driver.current_url)
print("Page Title :", driver.title)

# Verify successful login
message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("Login Successful")
else:
    print("Login Failed")

# Close browser
driver.quit()