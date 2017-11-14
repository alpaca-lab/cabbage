from selenium import webdriver
import time
def bilibili(fp):
    driver = webdriver.Firefox()
    driver.get(fp)
    elem = driver.find_element_by_name("play_button")
    elem.click()
    time.sleep(20)
    driver.close()

if __name__=="__main__":
    fp="https://www.bilibili.com/video/av16331381/"
    bilibili(fp)
