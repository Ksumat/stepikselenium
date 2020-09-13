from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    a = browser.find_element_by_css_selector('#num1')
    b = browser.find_element_by_css_selector('#num2')

    a1 = int(a.text)
    b1 = int(b.text)
    sum =a1+b1
    select = Select(browser.find_element_by_tag_name("select"))
    sum=str(sum)
    print(sum)
    select.select_by_visible_text(sum)
    print('dsfsg')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
