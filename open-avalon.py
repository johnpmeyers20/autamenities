import os
import time  # This is necessary to delay the closing of the window later. This module is included w/ python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('./.env') as f:
    content = f.readlines()

# for this to work the format in the .env file has to be very specific USERNAME='jp' - no spaces etc.
content = [x.strip().split('=') for x in content]

for line in content:
    os.environ[line[0]] = line[1]

# Create a new browser instance
browser = webdriver.Chrome()

# Navigate to the website's login page
browser.get("https://www.avalonaccess.com/UserProfile/LogOn")

# Find the username and password fields and enter your login information
username_field = browser.find_element(By.ID, "UserName")
password_field = browser.find_element(By.ID, "password")
username_field.send_keys(os.environ.get('USERNAME'))
password_field.send_keys(os.environ.get('PASSWORD'))

# Find and click the login button
login_button = browser.find_element(By.ID, "submit-sign-in")
login_button.click()

# The following applies to the second page presented. (1st after login);
# wait = WebDriverWait(browser, 3)
# information_button = wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#Information a")))
information_button = browser.find_element(By.CSS_SELECTOR, "#Information a")
information_button.click()

# 3rd Page
amenities_button = browser.find_element(By.CSS_SELECTOR, "#Amenities a")
amenities_button.click()

reserve_racquetball_button = browser.find_element(
    By.CSS_SELECTOR, "input[data-amenity='ea434ccd-bdf4-458c-8ae5-d27fbc38ea13']")
reserve_racquetball_button.click()

time.sleep(10)  # This command keeps the window open for 10 seconds
browser.quit()
