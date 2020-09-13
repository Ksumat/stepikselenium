import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

submit = browser.find_element_by_tag_name("button").click()
#confirm = browser.switch_to.alert
#confirm.accept()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)

button = browser.find_element_by_tag_name('button').click()


time.sleep(10)
browser.quit()