'''Задание 1 Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария:

from selenium import webdriver
browser = webdriver.Chrome()
#browser.execute_script("alert('привет тупица нажми ок');")
Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой.
Изменим сначала заголовок страницы, а затем вызовем alert:
browser.execute_script("document.title='Script executing';alert('Robots at work');")'''

'''Задание 2 Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть на элемент, который 
внезапно оказывается перекрыт другим элементом на странице.'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Выдаст ошибку так как кнопу закрывает огромный футер
# button = browser.find_element(By.TAG_NAME, "button")
#button.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
#Эта команда проскроллит страницу на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.TAG_NAME, "button")
    time.sleep(3)
    _ = button.location_once_scrolled_into_view
    # или browser.execute_script("window.scrollBy(0, 150);")
    time.sleep(3)
    button.click()

