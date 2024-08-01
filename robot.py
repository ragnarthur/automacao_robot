from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # Importar as exceções necessárias
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

LOGIN_URL = os.getenv('LOGIN_URL')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def cadastro_web(dataframe):
    # Inicializando o navegador
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(LOGIN_URL)

    try:
        # Fazendo login
        email = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        email.send_keys(EMAIL)
        time.sleep(1)
        email.send_keys(Keys.TAB)

        password = browser.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys(PASSWORD)

        time.sleep(1)

        botao_entrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_entrar.click()

        # Esperar o login completar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]")))

        # Iterando sobre as linhas do dataframe
        for _, linha in dataframe.iterrows():
            browser.get('http://automacao.empowerdata.com.br/index.php?page=cadastro_cliente')
            
            # Preenchendo o formulário
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nome"]')))
            cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
            cliente.send_keys(linha['Nome'])
            email = browser.find_element(By.XPATH, '//*[@id="email"]')
            email.send_keys(linha['E-mail'])
            telefone = browser.find_element(By.XPATH, '//*[@id="telefone"]')
            telefone.send_keys(linha['Telefone'])
            cidade = browser.find_element(By.XPATH, '//*[@id="cidade"]')
            cidade.send_keys(linha['Cidade'])
            estado = browser.find_element(By.XPATH, '//*[@id="estado"]')
            estado.send_keys(linha['Estado'])

            time.sleep(1.5)

            botao_cadastrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
            botao_cadastrar.click()

            # Esperar o cadastro completar
            time.sleep(3)

    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        browser.quit()
