#Задание: поиск элемента по тексту в ссылке
'''В этой задаче мы попробуем искать элементы по тексту ссылки, для этого
воспользуемся методом find_element_by_link_text:
Задание
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

Добавьте в самый верх своего кода import math
Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
str(math.ceil(math.pow(math.pi, math.e)*10000))
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)

Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

Заполните скриптом форму так же как вы делали в предыдущем шаге урока'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

x=str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, x)
    link.click()

    input1 = browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country").send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
