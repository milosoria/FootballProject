from selenium import webdriver
import os
driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
driver.get("https://www.goal.com/es-cl")
