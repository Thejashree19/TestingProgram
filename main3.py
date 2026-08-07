from selenium import webdriver
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# ----------------------------
# Open First Website
# ----------------------------
driver.get("https://www.google.com")
print("First Website :", driver.title)

time.sleep(2)

# ----------------------------
# Open New Tab
# ----------------------------
driver.switch_to.new_window('tab')

# Open Second Website
driver.get("https://www.wikipedia.org")
print("Second Website :", driver.title)

time.sleep(2)

# ----------------------------
# Store Window Handles
# ----------------------------
tabs = driver.window_handles

# Switch to First Tab
driver.switch_to.window(tabs[0])
print("Switched to First Tab :", driver.title)

time.sleep(2)

# Switch to Second Tab
driver.switch_to.window(tabs[1])
print("Switched to Second Tab :", driver.title)

time.sleep(2)

# ----------------------------
# Back Navigation
# ----------------------------
driver.get("https://www.python.org")
time.sleep(2)

driver.back()
print("After Back :", driver.title)

time.sleep(2)

# ----------------------------
# Forward Navigation
# ----------------------------
driver.forward()
print("After Forward :", driver.title)

time.sleep(2)

# ----------------------------
# Refresh
# ----------------------------
driver.refresh()
print("Page Refreshed")

time.sleep(2)

# ----------------------------
# Close Current Tab
# ----------------------------
driver.close()

# ----------------------------
# Switch Back to First Tab
# ----------------------------
driver.switch_to.window(tabs[0])

print("Current Tab :", driver.title)

time.sleep(2)

# Close Browser
driver.quit()