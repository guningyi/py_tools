#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

opt = webdriver.ChromeOptions()   #创建浏览
# opt.headless = True
# opt.set_headless()    #无窗口模式
driver = webdriver.Chrome(options=opt)  #创建浏览器对象

while 1:
    print(time.time())
    driver.get('https://h5cdn.cretech.cn/v/U130599LD9H?toPage=1362242') #打开网页
    # driver.maximize_window()   #最大化窗口
    # driver.minimize_window()
    time.sleep(2)     #加载等待

    str_lowlevel = '//*[@id="next_page"]/div'
    driver.find_element_by_xpath(str_lowlevel).click()
    time.sleep(2)     #加载等待

    str_lowlevel = '//*[@id="4308010178"]'
    driver.find_element_by_xpath(str_lowlevel).click()
    # time.sleep(1)     #加载等待

    # t1 = driver.find_element_by_xpath(str_path).get_attribute("data-counter-number")
    # print(t1)

    str_button = '//*[@id="7996662488"]/div/i'
    a = driver.find_element_by_xpath(str_button)
    ActionChains(driver).move_to_element(a).perform()
    driver.execute_script("arguments[0].click();", a)

    str_path = '//*[@id="7996662488"]/div/span'
    t2 = driver.find_element_by_xpath(str_path).get_attribute("data-counter-number")
    print(t2)

    # driver.close()