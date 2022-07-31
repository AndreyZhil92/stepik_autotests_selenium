'''когда мы уже знаем, что кнопка появляется с задержкой, мы можем добавить паузу до начала поиска
элемента.Мы уже использовали библиотеку time ранее.Давайте применим ее и сейчас'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text


Надеемся, вы поняли, что решение с time.sleep() плохое: оно не масштабируемое и трудно поддерживаемое.
Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов из-за асинхронной
работы скриптов или задержек от сервера, поэтому мы будем ждать появление элемента на странице в течение заданного
количества времени (например, 5 секунд). Проверять наличие элемента будем каждые 500 мс. Как только элемент будет
найден, мы сразу перейдем к следующему шагу в тесте. Таким образом, мы сможем получить нужный элемент в идеальном
случае сразу, в худшем случае за 5 секунд.

В Selenium WebDriver есть специальный способ организации такого ожидания, который позволяет задать ожидание при 
инициализации драйвера, чтобы применить его ко всем тестам. Ожидание называется неявным (Implicit wait),
 так как его не надо явно указывать каждый раз, когда мы выполняем поиск элементов, оно автоматически будет применяться 
 при вызове каждой последующей команды.
Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep() и добавить одну строчку с 
методом implicitly wait:'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

