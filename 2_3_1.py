'''Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
alert = browser.switch_to.alert #Кстати browser.switch_to_alert().accept() считается устаревшим, рекомендуется использовать browser.switch_to.alert.accept().
alert.accept()

def cap(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = cap(x)
print(x)
print(y)

option = browser.find_element(By.ID, "answer").send_keys(cap(x))
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

time.sleep(10)
browser.quit()
