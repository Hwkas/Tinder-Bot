from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# constants
CHROME_DRIVER_PATH = "Your chromedriver path"
URL = "https://tinder.com/"

#setting up selenium
service_obj = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service_obj)
driver.get(url=URL)

time.sleep(2)
cookie_decline_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()

# getting hold of login button
login_btn = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

time.sleep(2)
try:
    # getting hold of login with google button
    loginwfb = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    loginwfb.click()
except:
    # getting hold of more options button
    more_options_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/button')
    more_options_btn.click()
    # getting hold of login with google button
    loginwfb = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    loginwfb.click()

time.sleep(2)
# chaging the focus of selenium to the facebook authentication tab.
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# printing the title of the tab/website we are currently on to check we are on the fb authentication tab
print(driver.title)
# getting hold of the email field & sending/typing the email address
email_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_field.send_keys("Your Email")
# getting hold of the password field & sending/typing the password 
password_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_field.send_keys("Your Password")
password_field.send_keys(Keys.ENTER)
# adding wait time, so that the tider loads after loggin
time.sleep(20)
# getting back the focus of selenium of tider tab/window
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)

try:
    # getting hold of allow location button & allowing location access
    location_allow_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
    location_allow_btn.click()
except:
    time.sleep(10)
    # getting hold of allow location button & allowig location access
    location_allow_btn = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span').click()

time.sleep(1)
# getting hold of notification button & declining the notifications
notification_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span').click()
# loop to automatically swipe for 100 times , 100 because the free tier only gives 100 swipes per day
time.sleep(20)
for n in range(0, 100):
    time.sleep(1)
    # getting hold of like button
    like_btn = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)

print("That all the swipes for today, Run me tomorrow again")

driver.quit()
