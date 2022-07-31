#Задание: поиск элемента по XPath
'''На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации,
как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только
 кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.

Ваши шаги:

В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.'''


'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/find_xpath_form'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    inputs = browser.find_elements(By.XPATH, "//*[@class='form-group']/ input")
    for i in inputs:
        i.send_keys('qwerty')
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[ text()='Submit']").click()

    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    alert.accept()'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form" #ссылка

try:
    browser = webdriver.Chrome()
    browser.get(link) #переход по ссылке

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country").send_keys("Russia") #можно так кликать в одной строке
    button = browser.find_element(By.XPATH, "//*[ text()='Submit']")
    button.click()

finally:
    driver.close()
    time.sleep(30) # успеваем скопировать код за 30 секунд
    browser.quit() # закрываем браузер после всех


'''import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrome_options = Options()
    driver_service = Service("C:\\chromedriver\\chromedriver.exe")

    starter_link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome(service=driver_service, options=chrome_options)
        browser.get(starter_link)
        time.sleep(1)

        elements = browser.find_elements(By.CSS_SELECTOR, "input[type=\"text\"]")

        for element in elements:
            element.send_keys("random text")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"")
        submit_button.click()

        alert = browser.switch_to.alert
        print("The code from pop-up window is: ", alert.text.split()[-1])
        alert.accept()

    finally:
        browser.close()
        time.sleep(2)
        browser.quit()'''