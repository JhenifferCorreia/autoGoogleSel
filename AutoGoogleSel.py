from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

# *** VARIAVEIS
strUrl = 'https://www.google.com'
strTextToSearch = "TwitchAlanzoka"


# *** DRIVERS
driver = webdriver.Chrome()
# *** PASSO 01: Abre o navegador e carrega a URL 
driver.get(strUrl)

# *** PASSO 02: Verifica se o elemento de busca foi encontrado com sucesso ou ocorreu algum erro.
isOk = driver.find_element_by_name('q')

if isOk:
    print('PASSO 01: O campo de pesquisa foi encontrado: SUCESSO')
else:
    print('PASSO 01: O campo de pesquisa foi encontrado: ERRO')


# *** PASSO 03: Pesquisa o o nome inserido na variavel strTextToSearch
driver.find_element_by_name('q').send_keys(strTextToSearch + Keys.ENTER)

validacaoDeBusca = driver.find_elements_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')

if validacaoDeBusca:
    print('Busca encontrada com sucesso')
else:
    print('Busca não encontrada')
 

# *** PASSO 04: Endereço de um elemento HTML e clique
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()


time.sleep(2)

