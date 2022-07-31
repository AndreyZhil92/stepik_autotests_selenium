'''Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно
переключить WebDriver на новую вкладку и решить в ней задачу.
Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

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

'''from selenium import webdriver
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(1)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.trollface.btn").click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ

    # Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Копируем результат
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

    # Нажимаем на кноку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием

    browser.get("https://stepik.org")
    time.sleep(5)
    # или можно было перейти сразу по ссылке browser.get("https://stepik.org/catalog?auth=login") и тогда след.строчка не нужна
    browser.find_element_by_css_selector(".navbar__links .navbar__auth_type_login").click()

    browser.find_element_by_id("id_login_email").send_keys("email")
    browser.find_element_by_id("id_login_password").send_keys("password")
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(4)

    browser.get("https://stepik.org/lesson/184253/step/6")
    time.sleep(5)

    # Находим поле для ввода ответа
    textarea = browser.find_element_by_css_selector(".textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)

    # Напишем текст ответа в найденное поле
    textarea.send_keys(addToClipBoard)

    # Отправляем ответ
    browser.find_element_by_css_selector(".submit-submission").click()

    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()'''

