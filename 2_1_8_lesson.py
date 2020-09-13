from selenium import webdriver
import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'step.txt')

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

browser.get(link)
input = browser.find_element_by_xpath('//input[@name="firstname"]')
input.send_keys('Kseniya')
input1 = browser.find_element_by_xpath('//input[@name="lastname"]')
input1.send_keys('matush')
input2 = browser.find_element_by_xpath('//input[@name="email"]')
input2.send_keys('aigfdhg@mail.com')
file = browser.find_element_by_css_selector('#file')
file.send_keys(file_path)

submit = browser.find_element_by_tag_name("button").click()

time.sleep(10)
browser.quit()