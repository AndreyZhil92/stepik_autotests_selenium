'''смысл задания.
Смысл в том, чтобы запустив код (например мой вариант), увидеть в консоли как отработает код и выбросит
исключение: NoSuchElementException. Результатом решения задачи, было увидеть данное сообщение и выбрать его из
предложенных.'''

from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

browser.find_element_by_id("button")
button.click()

assert "successful" in message.text

time.sleep(7)
browser.quit()

