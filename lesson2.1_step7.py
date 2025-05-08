from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    option = browser.find_element(By.ID,"robotCheckbox")
    option.click()

    option1 = browser.find_element(By.ID,"robotsRule")
    option1.click()

    option2 = browser.find_element(By.CLASS_NAME,"btn-default")
    option2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()