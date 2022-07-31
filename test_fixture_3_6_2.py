import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

x = math.log(int(time.time()))

link = "https://stepik.org/lesson/236895/step/1"

browser = webdriver.Chrome()
browser.get(link)

unput1 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "quiz-plugin"))).send_keys(x)

button = browser.find_element(By.CLASS_NAME, "submit-submissions")
button.click()

browser.quit()







'''@pytest.mark.parametrize('link', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_see_link(browser, var):
    link = f"https://stepik.org/lesson/{link}/step/1/"
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "quiz-plugin").send_keys("answer")
    print(test_see_link)'''