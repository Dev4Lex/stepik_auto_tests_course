from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys("name")

    input2 = browser.find_element(By.NAME,"lastname")
    input2.send_keys("lastname")

    input3 = browser.find_element(By.NAME,"email")
    input3.send_keys("email")

    element = browser.find_element(By.NAME,"file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME,"btn-primary")
    submit_button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()