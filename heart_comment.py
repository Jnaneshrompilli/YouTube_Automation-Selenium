from selenium import webdriver
import time
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By


option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:8797")
option.add_experimental_option("debuggerAddress", "localhost:8797")

driver = webdriver.Chrome(executable_path = "D:\API\chromedriver.exe",options=option)

driver.get("https://studio.youtube.com/video/cUyzrDHzQNI/comments/inbox?filter=%5B%7B%22name%22%3A%22ENGAGED_STATUS%22%2C%22value%22%3A%22COMMENT_CATEGORY_NOT_ENGAGED%22%7D%5D")



time.sleep(5)

for i in range(0, 1):
    #driver.find_element_by_id('unhearted').click()
    element  = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='unhearted']")))
    element.click()
    driver.refresh()
    #time.sleep(15)



