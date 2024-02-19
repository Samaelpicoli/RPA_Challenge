import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import requests


from traducao import Tradutor

class Desafio(Tradutor):
    #Essa classe possui todas as funcionalidades para executar o bot no site RPA Challenge
    
    def __init__(self):
        #instanciando as classes que estão sendo herdadas
        self.tradutor = Tradutor()
        #abrindo o rpa challenge
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-notifications")
        self.options.add_experimental_option("prefs", { "download.default_directory": os.path.dirname(os.path.realpath(__file__))})
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)
        self.wdw = WebDriverWait(self.driver, 40)
        self.driver.maximize_window()
        
    def acessa_site(self, url: str):
        #inicia o site rpa challenge
        try:
            self.driver.get(url)
            self.wdw.until(ec.visibility_of_element_located((By.CLASS_NAME, 'btn-large')))
        except Exception as error:
            print(f'Erro ao iniciar o site: {error}')
            raise Exception('Erro ao iniciar o Site')

    def inicia_desafio(self):
        #aperta o botão start para iniciar a inclusão dos dados
        try:
            self.driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
        except Exception as error:
            print(f'Erro ao iniciar o desafio: {error}')
            raise Exception('Erro ao iniciar o desafio')

    def download_arquivo(self):
        #faz a requisição, traz o arquivo para máquina e faz a leitura do mesmo
        try:
            url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
            arquivo = requests.get(url, allow_redirects=True)
            open('challenge.xlsx', 'wb').write(arquivo.content)
            dados = pd.read_excel('challenge.xlsx')
            return dados
        except Exception as error:
            print(f'Erro ao fazer o download do arquivo: {error}')
            raise Exception('Erro ao fazer o download do arquivo')


    def inserindo_dados(self, dados):
        #faz a inserção dos dados no processo
        for index, row in dados.iterrows():
            try:
                self.driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]').send_keys(row['First Name'])
                self.driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]').send_keys(row['Last Name '])
                self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]').send_keys(row['Company Name'])
                self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]').send_keys(row['Role in Company'])
                self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]').send_keys(row['Address'])
                self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]').send_keys(row['Email'])
                self.driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]').send_keys(row['Phone Number'])
                self.driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
                linha = index + 1
            except Exception as error:
                linha = index + 1
                print(f'Erro ao inserir os dados da linha {linha}. Detalhes: {error}')
                raise Exception(f'Erro ao inserir os dados da linha {linha}')

    def captura_tempo(self):
        #faz a captura do tempo que o robô levou para executar o processo
        try:
            mensagem = self.wdw.until(ec.visibility_of_element_located((By.CLASS_NAME, 'message2')))
            if '100%' in mensagem.text:
                msg = self.tradutor.traduzir(mensagem.text)
                print(msg)
                self.driver.save_screenshot('challenge.png')
                return True
        except Exception as error:
            print(f'Erro durante a inserção dos dados. Detalhes: {str(error)}')
            raise Exception('Erro durante a inserção dos dados.')
    
    def fecha_navegador(self):
        #fecha o driver
        self.driver.close()

    def __del__(self):
        #deleta a instância da classe
        print('Fim da execucao')



