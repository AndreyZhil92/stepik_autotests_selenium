'''Решил побаловаться тем, что уже прошел на этом курсе: ставлю свою версию скрипта, который автоматом полученный ответ с
страниц заданий отправляет на stepik в форму заполнения ответа'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def send_answer(answer, lessonURL):
    browser = webdriver.Chrome()
    email = '****@***.***'  ## Mail to log in with
    password = '************'  ## Password

    browser.get(lessonURL)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/course/575/promo?auth=login']")))
    current_url = str(browser.current_url)
    browser.find_element(By.XPATH, "//a[@href='/course/575/promo?auth=login']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[ name = "login"]')))
    browser.find_element(By.CSS_SELECTOR, '[ name = "login"]').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, '[name = "password"]').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
    time.sleep(2)  ## Так и не понял почему, но без time.sleep метод get отказывается работать
    browser.get(lessonURL)
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")))
    browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").clear()
    browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").send_keys(answer)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class ="submit-submission"]')))
    browser.find_element(By.CSS_SELECTOR, 'button[class ="submit-submission"]')

    ## Всё это дело вызываю в конце каждого задания, сохраняя ответ в answer и указывая ручками ссылку на урок - lessonURL в файле с уроком
    ## Код выше работает только для заданий, которые ещё не были выполнены - поленился добавить эту фичу, поэтому на сделанных уже заданиях будете получать InvalidElementStateException. Для проверки можно самому нажать на странице "Выполнить ещё раз" и прогнать этот код

