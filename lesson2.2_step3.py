from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sum1 = int(browser.find_element(By.ID,"num1").text)
    sum2 = int(browser.find_element(By.ID,"num2").text)
    summa = str(sum1 + sum2)

    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(summa)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()