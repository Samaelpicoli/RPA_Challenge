import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#lendo o arquivo xlsx
arquivo = 'challenge.xlsx'
df = pd.read_excel(arquivo)

#abrindo o rpa challenge
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://rpachallenge.com/')
driver.maximize_window()
WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')))
driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

#loop e inserindo os dados 
for index,row in df.iterrows():
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]').send_keys(row['First Name'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]').send_keys(row['Last Name'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]').send_keys(row['Company Name'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelRole"]').send_keys(row['Role in Company'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]').send_keys(row['Address'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelEmail"]').send_keys(row['Email'])
    driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelPhone"]').send_keys(row['Phone Number'])
    driver.find_element(By.XPATH, '//input[@value="Submit"]').click()

#driver.close()
