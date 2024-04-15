from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('http://google.com')
driver.maximize_window()
input('Нажми кнопку для продолжения...')

with open('result_1.txt', 'r') as file:
    persons = file.readlines()
    for person in persons:
        if person != '':
            print(person)
            driver.get('http://google.com')
            enter_search = driver.find_element(By.TAG_NAME, 'textarea')
            enter_search.send_keys(f'site:linkedin.com/in intitle:{person}')
            try:
                enter_search.send_keys(Keys.ENTER)
            except:
                pass
            
            time.sleep(2) 