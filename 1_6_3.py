'''Задание: использование метода find_elements
В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях
своего продукта. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей
и ограничив время на ее заполнение.

Используйте WebDriver, метод find_elements, нужные локатор и его значение. Введите полученный код в
качестве ответа к этой задаче.

Используйте приведенный ниже шаблон: в цикле for мы можем последовательно взять каждый элемент из
найденного списка текстовых полей и отправить произвольный текст в каждое поле. Если скрипт не
успевает заполнить форму, выберите текст покороче.'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')

    for element in elements:
        element.send_keys('Z')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()


'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/huge_form.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    [i.send_keys('werty') for i in browser.find_elements(By.CSS_SELECTOR, '.first_block input')]
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(30)'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Курва")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(15)
    '''



'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, '//*[@type="text"]')
    for element in elements:
        element.send_keys("test")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    '''



