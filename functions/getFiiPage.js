// const puppeteer = require('puppeteer');
import puppeteer from "puppeteer";

const FII_CRI_LIST = [ 'CSHG CRI' ]

async function getFiiSearchPage(page){
  setTimeout( async () => {
    // Espera até que o modal esteja disponível na página
    const modal = await page.waitForSelector(' #myModalFiltros', { timeout: 210000 });

    // Espera até que o input dentro do modal esteja disponível na página
    const input = await modal.waitForSelector('ul > li > #s2id_autogen8', { timeout: 210000 });
  
    // Insere o texto no input
    await input.type(FII_CRI_LIST[0]);

    
    // espera o dado aparecer na tela e confirma busca
    setTimeout( async () => {
      await page.keyboard.press('Enter');
      const confirmSearch = await page.waitForSelector(' #filtrar', { timeout: 1000 });
      await confirmSearch.click()
    }, 1000)
  }, 1000)
}

async function run() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Navega até a página
  await page.goto('https://fnet.bmfbovespa.com.br/fnet/publico/abrirGerenciadorDocumentosCVM');

  // Espera até que o botão "EXIBIR FILTROS" esteja disponível na página
  const filterButton = await page.waitForSelector('#showFiltros', { timeout: 210000 });
  
  // Clica no botão "EXIBIR FILTROS"
  await filterButton.click();

  // Insere texto no campo de busca dentro do modal
  await getFiiSearchPage(page);
}

export { run }