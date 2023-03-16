// const puppeteer = require('puppeteer');
import puppeteer from "puppeteer";
import { getData } from "./getFiiInfos.js";
import { FIIS_LIST } from "../db/fiisList.js";

async function getFiiInfosPage(page){
  setTimeout( async () => {
    // Espera até que o modal esteja disponível na página
    const modal = await page.waitForSelector(' #myModalFiltros', { timeout: 210000 });

    // Espera até que o input dentro do modal esteja disponível na página
    const input = await modal.waitForSelector('ul > li > #s2id_autogen8', { timeout: 210000 });
  
    // Insere o texto no input
    await input.type(FIIS_LIST[0]);

    
    // espera o dado aparecer na tela e confirma busca
    setTimeout( async () => {
      await page.keyboard.press('Enter');
      const confirmSearch = await page.waitForSelector(' #filtrar', { timeout: 1000 });
      await confirmSearch.click()
    }, 1000);

    getData();
  }, 1000)
}

async function createEnvironment() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Navega até a página
  await page.goto('https://fnet.bmfbovespa.com.br/fnet/publico/abrirGerenciadorDocumentosCVM');

  // Espera até que o botão "EXIBIR FILTROS" esteja disponível na página
  const filterButton = await page.waitForSelector('#showFiltros', { timeout: 210000 });
  
  // Clica no botão "EXIBIR FILTROS"
  await filterButton.click();

  await getFiiInfosPage(page);
}

async function run() {
  createEnvironment();
}

export { run }