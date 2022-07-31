'''Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname").send_keys("Andrey")
input2 = browser.find_element(By.NAME, "lastname").send_keys("Zhilin")
input3 = browser.find_element(By.NAME, "email").send_keys("az@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
file_name = "file.txt"# имя файла, который будем загружать на сайт
file_path = os.path.join(current_dir, file_name)# получаем путь к file_example.txt
input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)#нажимаем кнопку и отправляем файл

button = browser.find_element(By.CSS_SELECTOR, "button.btn").click() #отправляем

time.sleep(5)
browser.quit()



