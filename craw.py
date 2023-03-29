from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime
from db import THE_DB, FIIS_LIST


print(datetime.datetime.now())
driver = webdriver.Chrome()
driver.get('https://fnet.bmfbovespa.com.br/fnet/publico/abrirGerenciadorDocumentosCVM')

for i, fii in enumerate(FIIS_LIST):
    print(f"{i}/{len(FIIS_LIST)} | {fii}")


    open_modal = driver.find_element(By.ID, "showFiltros")
    open_modal.click()


    driver.implicitly_wait(5)
    search_bar = driver.find_element(By.ID, 's2id_autogen8')
    if (len(THE_DB)) > 0:
        try:
            search_bar.send_keys(Keys.BACKSPACE)
            search_bar.send_keys(Keys.BACKSPACE)
            search_bar.send_keys(Keys.BACKSPACE)
        except:
            driver.find_elements(By.TAG_NAME, 'a')[2].click()
    search_bar.send_keys(f'{fii}')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'select2-result-label').click()
    try:
        driver.find_element(By.CLASS_NAME, 'select2-result-label').click()
    except:
        pass
    time.sleep(1)


    filterBtn = driver.find_element(By.ID, 'filtrar')
    filterBtn.click()


    time.sleep(3)
    pagina_atual = driver.page_source
    soup = BeautifulSoup(pagina_atual, 'html.parser')



    lista = []
    max_screen_exibition = driver.find_element(By.NAME, 'tblDocumentosEnviados_length').find_elements(By.TAG_NAME, 'option')[-1]
    max_screen_exibition.click()
    time.sleep(1)
    pagesQt = soup.find_all('a')
    pagesQt = int(pagesQt[-2].text)
    for i in range(0, pagesQt, 1):
        time.sleep(3)
        pagina_atual = driver.page_source
        soup = BeautifulSoup(pagina_atual, 'html.parser')
        infos = soup.find_all('tr')
        for all_infos in infos:
            info = all_infos.find_all('td')
            try:
                the_object = {'nome': info[0].text, 
                              'categoria': info[1].text, 
                              'tipo':  info[2].text, 
                              'data_ref': info[4].text, 
                              'data_ent': info[5].text,
                             'view_doc': '',
                             'download_doc': ''}
                lista.append(the_object)
            except:
                pass
        
        driver.find_element(By.ID, 'tblDocumentosEnviados_next').click()
    THE_DB[fii] = lista
    

print(datetime.datetime.now())