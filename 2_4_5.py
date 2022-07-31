'''Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более
высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
из библиотеки expected_conditions.'''


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

def formula(x): #расчет
    return str(math.log(abs(12 * math.sin(int(x)))))

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #Ждем пока цена не станет == заданой но не более 12 сек
if button == True:
    btn = browser.find_element(By.ID, 'book')
    btn.click()

time.sleep(1)

browser.execute_script("window.scrollBy(0, 170);") #Проскроллить страницу вниз  на ...px пикселей

x_element = browser.find_element(By.ID, "input_value") #число для расчета
x = x_element.text
y = formula(x)
print(x, y)

option = browser.find_element(By.ID, "answer").send_keys(formula(x)) #вставляем значение

button1 = browser.find_element(By.ID, "solve").click()

time.sleep(10)
browser.quit()

'''мой джентельменский набор, который
подгружаетдрайвер каждый раз, при запуске теста)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)'''