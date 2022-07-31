'''Задание: Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

browser.get('https://suninjuly.github.io/selects1.html')

x = browser.find_element(By.ID,"num1").text
y = browser.find_element(By.ID, "num2").text
sum = int(x) + int(y)
print(sum)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum)) #передается строка
browser.find_element(By.TAG_NAME,"button").click()
browser.quit()


'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "https://suninjuly.github.io/selects1.html"
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID,"num1").text
    y = browser.find_element(By.ID,"num2").text
    summ = int(x) + int(y)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("{}".format(summ))
    browser.find_element(By.TAG_NAME,"button").click()
finally:
    time.sleep(10)
    browser.quit()'''


'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)

x = str(eval('+'.join([i.text for i in browser.find_elements(by=By.CLASS_NAME, value="nowrap") if i.text.isdigit()][-3:])))
Select(browser.find_element(by=By.TAG_NAME, value="select")).select_by_value(x)
browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()'''




