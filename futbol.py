from selenium import webdriver
import os
driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
driver.get("https://www.uefa.com/uefachampionsleague/fixtures-results/#/rd/2001141/2")
first = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]')
first.click()
real_m = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[2]/div/div[67]/input')
juventus = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[2]/div/div[46]/input')
f_barcelona = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[2]/div/div[18]/input')
b_munich = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[2]/div/div[21]/input')
man_city = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[2]/div/div[56]/input')
teams = [real_m, juventus, b_munich, man_city]
for team in teams:
    team.click()
add_calendar = driver.find_element_by_xpath('//*[@id="calendar-service_teams-wrapper-modal"]/div/div/div[3]/div/a')
add_calendar.click()
skip = driver.find_element_by_xpath('//*[@id="calendar-service-modal"]/div/div/a')
skip.click()
copy_link = driver.find_element_by_xpath('//*[@id="calendar-service-not_iosOrMac-modal"]/div/div/div[1]/div[2]/div/div[1]/a')
copy_link.click()
print(copy_link)