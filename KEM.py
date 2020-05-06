from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup as BS
### 26 letras, len =6
driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
driver.get("https://www.kemxtreme.cl/")
explorando = True
encontrado = False
try:
    while explorando:
        element = driver.find_element_by_xpath('//*[@id="generado"]')
        time.sleep(1)
        element = element.get_attribute('value')
        input_1 = driver.find_element_by_xpath('//*[@id="form"]/fieldset/input')
        input_1.send_keys(element)
        send_button = driver.find_element_by_xpath('//*[@id="enviar"]')
        send_button.click()
        time.sleep(1)
        soup = BS(driver.page_source, features = "html.parser")
        for item in soup.find_all(['div', 'h1']):
            if item.text.strip().find("sigue participando :( ¡hay millones de oportunidades!") != -1:
                print("no ganaste")
                print(element)
                driver.find_element_by_xpath('//*[@id="principal"]/div[2]/div[3]/a').click()
                encontrado = True
                break
        if not encontrado:
            explorando = False
            print("GANASTE!")
            print(element)
except:
    print("GANASTE!")
    print(element)