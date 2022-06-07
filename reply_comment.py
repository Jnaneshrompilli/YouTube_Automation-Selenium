import pyautogui
from selenium import webdriver
import time
import pyautogui
from  selenium.webdriver import  ActionChains
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:8797")
option.add_argument('window-size=1920,1080')
option.headless = True


driver = webdriver.Chrome(executable_path = "D:\API\chromedriver.exe",options=option)

driver.get("https://studio.youtube.com/channel/UCs5osGMasejiyBh8NcMOO7w")

time.sleep(4)

driver.find_element_by_id('menu-paper-icon-item-4').click()

replies = ("Subscribe !","God Bless You !","LOL","Something is wrong. I can feel it","Hello !", "WTH", "MyBoi","HaHa")

for i in range(0,10):
    time.sleep(7)
    driver.find_element_by_xpath("//*[@class='style-scope ytcp-comment-button style-text size-default']").click()
    btn = driver.find_element_by_xpath("//*[@class='style-scope iron-autogrow-textarea']")
    btn.send_keys(f'{replies[i]}')
    btn.send_keys(Keys.CONTROL,Keys.ENTER)
    time.sleep(2)
    driver.refresh()
    time.sleep(6)


