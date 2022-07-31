'''Задание: уникальность селекторов
Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся. Также и вам
предстоит проверить чужой код. Ознакомившись с разными способами решения одной и той же задачи, вы сможете лучше понять
изучаемую тему.У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на
сайте. Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная
страница доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.
Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с
ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который
создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении
которое вы тестируете, а не в вашем тесте.
Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае попробуйте поменять
селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии страницы.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input1.send_keys("Ivan")
    time.sleep(2)

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")  #(By.XPATH, "//input")[1] - не уникальный поиск  https://www.w3schools.com/cssref/css_selectors.asp
    input2.send_keys("Petrov")
    time.sleep(2)

    '''input1 = browser.find_element(By.CLASS_NAME, "form-control.first")Такой поиск ищет два элемента: Поле - First name Поле - Phone Так как эти два поля имеют одинаковые классы: class="form-control first"
    Можно воспользоваться CSS_SELECTOR "div.first_block .form-control.first" для поля - First name'''

    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("@mail")
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

'''Вот так делать не надо т.к. на реальном проекте могут изменить порядок полей и тест упадет(например в поле телефон 
будет почта вводится). Чего не случится в случае если использовать всякие айдишники, классы, имена
input2 = browser.find_elements(By.XPATH, "//input")[1]
input2.send_keys("Petrov")

Примеры других учащихся

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")
    input3.send_keys("test@yandex.ru")



    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
    input3.send_keys("i.petrov@sample.com")
    
    
    
    input_first_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    input_first_name.send_keys("Name")

    input_last_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    input_last_name.send_keys("Last name")

    input_email = browser.find_element(
        By.CSS_SELECTOR, "div.form-group.third_class > input")
    input_email.send_keys("email")
'''

