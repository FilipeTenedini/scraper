from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://fnet.bmfbovespa.com.br/fnet/publico/abrirGerenciadorDocumentosCVM')

pagina_atual = driver.page_source
soup = BeautifulSoup(pagina_atual, 'html.parser')

open_modal = driver.find_element(By.ID, "showFiltros")
open_modal.click()

