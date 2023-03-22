#### my first webcrawler

### const browser = await puppeteer.launch({ headless: false });
    - abre o navegador
        - headless false define que você quer ver o navegador que o robô irá abrir, tem true por padrão que significa que ele ficará invisível.

### const page = await browser.newPage();
    - cria uma instancia do navegador para que você possa o controlar.
    
### await page.goto('seuSite');
    - te ajuda a navegar para tal página.

### waitForSelector(#seuSeletor)
    - aguarda que tal seletor apareça na página

### .click();
    - clica no elemento que você criar.

### Função para que ele aguarde essa função ser executada antes de prosseguir com o código
    - neste caso é uma função que aguarda pela alteração do estilo do elemento.
```
 await page.waitForFunction(() => {
            const element = document.querySelector('#tblDocumentosEnviados_processing');
            const style = window.getComputedStyle(element);
            return style.getPropertyValue('display') === 'none';
        });
```

### const announcements = await page.evaluate(async () => {} )
    - você consegue escrever codigo javascript para manipular o dom utilizado o page.evaluate();

