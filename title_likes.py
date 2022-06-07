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

action = ActionChains(driver)

driver.get("https://studio.youtube.com/video/cUyzrDHzQNI/analytics/tab-interest_viewers/period-default/explore?entity_type=VIDEO&entity_id=cUyzrDHzQNI&time_period=since_publish&explore_type=TABLE_AND_CHART&metric=LIKES_PER_LIKES_PLUS_DISLIKES_PERCENT&granularity=DAY&t_metrics=LIKES_PER_LIKES_PLUS_DISLIKES_PERCENT&t_metrics=RATINGS_LIKES&t_metrics=RATINGS_DISLIKES&dimension=VIDEO&o_column=LIKES_PER_LIKES_PLUS_DISLIKES_PERCENT&o_direction=ANALYTICS_ORDER_DIRECTION_DESC")

time.sleep(5)

count = driver.find_elements_by_xpath("//*[@class='value debug-metric-value style-scope yta-explore-table-row']")
#count = driver.find_element_by_class_name('value debug-metric-value style-scope yta-explore-table-row').text
print(count[1].text)
likes = count[1].text

driver.get("https://studio.youtube.com/video/cUyzrDHzQNI/edit")

btn1 = driver.find_element_by_id('textbox')
btn1.click()

action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
btn1.send_keys(f'Watch this, If you are Depressed !( Likes = {likes})')

time.sleep(5)

btn1 = driver.find_element_by_xpath("//*[@class='primary style-scope ytcp-entity-page-header']")
btn1.click()
pyautogui.press(['tab','tab','enter'])

