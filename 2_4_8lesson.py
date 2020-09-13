import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

browser.get(link)

price = browser.find_element_by_css_selector('#price')
book = browser.find_element_by_css_selector('#book')

eak = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
book.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)

button = browser.find_element_by_id('solve').click()

time.sleep(10)
browser.quit()
