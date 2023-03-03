import os
# it is important to import the datetime class of the datetime module
import datetime
import time  # This is necessary to delay the closing of the window later. This module is included w/ python
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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

# Tennis Court 1
reserve_tennis_court_1 = browser.find_element(
    By.CSS_SELECTOR, "input[data-amenity='40af5c05-9c86-463f-94d3-0e3d3c9a4965']")
reserve_tennis_court_1.click()

# Racquetball
# reserve_racquetball_button = browser.find_element(
#     By.CSS_SELECTOR, "input[data-amenity='ea434ccd-bdf4-458c-8ae5-d27fbc38ea13']")
# reserve_racquetball_button.click()

# 4th Page actual Racquetball Reservation page
date = browser.find_element(By.ID, "resv-date")
date.click()
now = datetime.date.today()
# the hyphen btwn the % and d removes the preceding 0 from single digit dates
# This part was tough. I needed a dynamic way to select tomorrow. the date doesn't work bc
# if today is 3 + 1 would be 4, but on the 31 + 1 would be 1.
today = now.strftime("%-d")
tomorrow = (now + datetime.timedelta(days=1)).strftime("%-d")
today_link = browser.find_element(By.LINK_TEXT, today)
tomorrow_link = browser.find_element(By.LINK_TEXT, tomorrow)
tomorrow_link.click()

reservation_time = browser.find_element(By.ID, "SelStartTime")
reservation_time.click()
specific_time = browser.find_element(
    By.CSS_SELECTOR, "#SelStartTime>option[value='Saturday-11:00 AM-12:00 PM ']")
specific_time.click()

number_of_people = browser.find_element(By.ID, "NumberOfPeople")
number_of_people.clear()  # This gets rid of the value that's already in the field
number_of_people.send_keys(1)  # 1 is the value I want in the field
reservation_names = browser.find_element(By.ID, "ReservationNames")
reservation_names.send_keys('John Meyers')

reserve_button = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
reserve_button.click()

# time.sleep(10)  # This command keeps the window open for 10 seconds
browser.quit()
