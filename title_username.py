"""
This Code updates title with username of most recent comment

"""
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:8797")
option.add_argument("window-size=1920,1080")
option.headless = True


driver = webdriver.Chrome(executable_path="D:\API\chromedriver.exe", options=option)

action = ActionChains(driver)

time.sleep(10)
driver.get(
    "https://studio.youtube.com/video/cUyzrDHzQNI/comments/inbox?filter=%5B%7B%22name%22%3A%22ENGAGED_STATUS%22%2C%22value%22%3A%22COMMENT_CATEGORY_NOT_ENGAGED%22%7D%5D"
)

time.sleep(5)

name = driver.find_element_by_xpath(
    "//*[@class='author-text style-scope ytcp-comment']"
).text

print(name)

driver.find_element_by_id("menu-paper-icon-item-0").click()
time.sleep(5)

btn1 = driver.find_element_by_id("textbox")
btn1.click()

action.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()
btn1.send_keys(f"Watch this, If you are Depressed !( Recent Comment By = {name})")

time.sleep(5)

btn1 = driver.find_element_by_xpath(
    "//*[@class='primary style-scope ytcp-entity-page-header']"
)
btn1.click()
pyautogui.press(["tab", "tab", "enter"])
