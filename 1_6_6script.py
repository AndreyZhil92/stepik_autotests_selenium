#Функция проверки элемента на уникальность (дляленивых)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def el_uniq_check(link: str, request: str, search_method=0):
    """
    Функция для проверки уникальности элемента
    Выведет сколько раз элемент встречается на странице

    link - ссылка на сайт
    request - запрос
    search_method - способ поиска элемента на странице(по умолчанию не выбран)
        search_method = 1 --> CSS-selector
        search_method = 2 --> XPath

    """

    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome(options=op)
    browser.get(link)
    if search_method not in (1, 2):
        search_method = input(
            "Если хотите искать с помощью CSS-Selector - введите 1\nЕсли хотите искать с помощью XPath - введите 2\n")
    if search_method in (1, '1'):
        element = browser.find_elements(By.CSS_SELECTOR, request)
    elif search_method in (2, '2'):
        element = browser.find_elements(By.XPATH, request)
    else:
        browser.quit()
        return None
    browser.quit()
    return len(element)


link = 'http://suninjuly.github.io/cats.html'
req = '//p[contains(text(), "cat")]'

print(el_uniq_check(link, req, 2))