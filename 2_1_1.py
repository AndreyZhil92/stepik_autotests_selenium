'''Задание: Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")  #x = browser.find_element(By.ID, "input_value").text -сокращенно
x = x_element.text
y = calc(x)

print(x)
print(y)

option = browser.find_element(By.ID, "answer").send_keys(calc(x))
option1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']").click()
option2 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

browser.quit()

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('button').click()
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()'''


'''from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()
radio = browser.find_element_by_id('robotsRule')
radio.click()
submit = browser.find_element_by_class_name('btn')
submit.click()

time.sleep(10)
browser.quit()'''