from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import time
from db import FIIS_LIST, THE_DB

# abre o chromium
driver = webdriver.Chrome()
driver.get('https://fnet.bmfbovespa.com.br/fnet/publico/abrirGerenciadorDocumentosCVM')

# itera o array com todos fiis listados
for fii in FIIS_LIST:

#   clica no botão para abrir o modal de procura
    open_modal = driver.find_element(By.ID, "showFiltros")
    open_modal.click()

#   digita o nome do fii
    driver.implicitly_wait(5)
    search_bar = driver.find_element(By.ID, 's2id_autogen8')
    if (len(THE_DB)) > 0: 
        time.sleep(1)
        driver.find_elements(By.TAG_NAME, 'a')[2].click()
    search_bar.send_keys(f'{fii}')
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, 'select2-result-label').click()


#   clica em filtrar
    filterBtn = driver.find_element(By.ID, 'filtrar')
    filterBtn.click()

#  aguarda e pega a página atual para passar ao soup
    time.sleep(3)
    pagina_atual = driver.page_source
    soup = BeautifulSoup(pagina_atual, 'html.parser')


#   cria uma lista que será populada
    lista = []
#   muda o número de infos na página para o máximo
    max_screen_exibition = driver.find_element(By.NAME, 'tblDocumentosEnviados_length').find_elements(By.TAG_NAME, 'option')[-1]
    max_screen_exibition.click()
    time.sleep(1)
#   pega o número de next que o bot terá que executar
    pagesQt = soup.find_all('a')
    pagesQt = int(pagesQt[-2].text)
#   itera, enquanto for menor que o número de next.
    for i in range(0, pagesQt, 1):
        time.sleep(3)
#   pega a página atual
        pagina_atual = driver.page_source
        soup = BeautifulSoup(pagina_atual, 'html.parser')

#       pega todos os trs que existem e itera
        infos = soup.find_all('tr')
        for all_infos in infos:
#       pega as linhas da tabela
            info = all_infos.find_all('td')
#       cria o objeto para popular a lista.
            try:
                the_object = {'nome': info[0].text, 'categoria': info[1].text, 'tipo':  info[2].text, 'data_ref': info[4].text, 'data_ent': info[5].text}
                lista.append(the_object)
            except:
                pass

#       muda de página
        driver.find_element(By.ID, 'tblDocumentosEnviados_next').click()

#   popula o DB
    THE_DB[fii] = lista
    

    
print(len(THE_DB))