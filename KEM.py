#Selenium
from selenium import webdriver
# Otros
import os
import time
import winsound
#BeautifulSoup4
from bs4 import BeautifulSoup as BS
def kem():
    try:
        duration = 3000  # milliseconds
        freq = 440  # Hz
        driver = webdriver.Chrome(os.getcwd() + "\\chromedriver.exe")
        driver.get("https://www.kemxtreme.cl/")
        explorando = True
        c = 0
        while explorando:
            encontrado = False
            c += 1
            time.sleep(2)
            element = driver.find_element_by_xpath('//*[@id="generado"]').get_attribute('value')
            driver.find_element_by_xpath('//*[@id="form"]/fieldset/input').send_keys(element)
            driver.find_element_by_xpath('//*[@id="enviar"]').click()
            time.sleep(2)
            soup = BS(driver.page_source, features = "html.parser")
            for c_1, item in enumerate(soup.find_all(['div', 'h1']), 1):
                if c_1 == 5:
                    if item.text.strip().find("sigue participando :( ¡hay millones de oportunidades!") != -1:
                        """print("No ganaste")
                        print(str(c) + "-" + str(element))"""
                        driver.find_element_by_xpath('//*[@id="principal"]/div[2]/div[3]/a').click()
                        encontrado = True
                        break
            if not encontrado:
                winsound.Beep(freq, duration)
                driver.maximize_window()
                print("GANASTE:" + element)
                time.sleep(20)
                # Busco qué gane
                try:
                    print([item.replace("\n", "") for item in soup.find_all(['div', 'h1'])])
                    print([item.replace("\n", "") for item in soup.find_all(['div', 'h1']) if item.find("GAME PASS") != -1 or item.find("XBOX") != -1])
                except Exception as e:
                    print("Sigue habiendo error en buscar el premio")
                    print(e)
                # Envío keys con datos a input boxes
                # Nombre
                driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[1]/input').send_keys('camilo pascal soria aranguiz')
                # Género
                driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[2]/select/option[3]').click()
                # Número de teléfono
                driver.find_element_by_xpath('//*[@id="form"]/div/div[5]/fieldset/input').send_keys("971083996")
                # Rut
                driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[3]/input').send_keys(
                    '202857442')
                # Edad
                driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/fieldset/input').send_keys(
                    '20')
                # Dirección
                driver.find_element_by_xpath('//*[@id="form"]/div/div[7]/fieldset[1]/input').send_keys(
                    'carmen tellez 4472')
                # Mail
                driver.find_element_by_xpath('//*[@id="form"]/div/div[7]/fieldset[2]/input').send_keys(
                    'camilo.soria@uc.cl')
                # Enviar
                driver.find_element_by_xpath('//*[@id="enviar"]').click()
                driver.get("https://www.kemxtreme.cl/")
    except Exception as e:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print("ERROR:", e)
        driver.quit()
        print("Reiniciando!")
        kem()
if __name__ == '__main__':
    kem()
