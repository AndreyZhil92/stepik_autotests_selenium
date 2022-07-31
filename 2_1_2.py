from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')

    checkbox_robot = browser.find_element(By.ID, 'robotCheckbox')
    default_attribute_checkbox_robot = checkbox_robot.get_attribute('checked')
    assert default_attribute_checkbox_robot == None, ' чекбокс не должен быть нажат по дефолту'

    radio_people = browser.find_element(By.ID, 'peopleRule')
    default_attrubure_radio_people = radio_people.get_attribute('checked')
    assert default_attrubure_radio_people, ' чекбокс должен быть нажат по дефолту'

    radio_robots = browser.find_element(By.ID, 'robotsRule')
    default_attribute_radio_robots = radio_robots.get_attribute('checked')
    assert default_attribute_radio_robots == None, ' чекбокс не должен быть нажат по дефолту'

finally:
    browser.quit()