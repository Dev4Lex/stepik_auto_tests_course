import os
import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get("https://stepik.org/lesson/236895/step/1")
    browser.implicitly_wait(15)
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    login_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_button.click()
    input_email = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    input_email.send_keys(email)
    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(password)

    submit_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']"))
    )
    submit_button.click()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', urls)
class TestParametrize:
    def test_parametrize(self, browser, url):
        browser.get(url)
        browser.implicitly_wait(15)
        answer = math.log(int(time.time()))

        input_answer = browser.find_element(By.CSS_SELECTOR, "textarea")
        input_answer.clear()
        input_answer.send_keys(str(answer))

        send_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        time.sleep(5)
        send_button.click()

        feedback = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")

        assert feedback.text == "Correct!", f"Expected 'Correct!', got '{feedback.text}'"
        if feedback.text == "Correct!":
            print(feedback.text)

if __name__ == "__main__":
    pytest.main()