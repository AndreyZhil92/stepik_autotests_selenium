'''Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.'''

import unittest
from selenium import webdriver
import time

class TestLinks(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.check_reg(link)

        self.assertEqual( welcome_text, "Congratulations! You have successfully registered!")

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.check_reg(link)

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    # Проверка одной страницы регистрации
    def check_reg(self, link):
        # print("Проверяем страницу: ", link)
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name("input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name("input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name("input[placeholder='Input your email']")
        input3.send_keys("123@example.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        time.sleep(3)
        browser.quit()

        return welcome_text

if __name__ == "__main__":
    unittest.main()
