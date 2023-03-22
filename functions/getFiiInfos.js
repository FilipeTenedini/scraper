async function getData(page){
    const allData = [];
    const pagesQt = await page.evaluate(() => Number(document.querySelector('#tblDocumentosEnviados_paginate > span > a:nth-child(7)').innerText)) //  é o nuumero máximo de page
    for (let i = 0; i < pagesQt; i++){

        await page.waitForFunction(() => {
            const element = document.querySelector('#tblDocumentosEnviados_processing');
            const style = window.getComputedStyle(element);
            return style.getPropertyValue('display') === 'none';
        });

        const announcements = await page.evaluate(async () => {

            const infos = []

            document.querySelectorAll('tbody tr').forEach(async (item) => {
                const fii = item.querySelectorAll('td')[0].innerText
                const categoria = item.querySelectorAll('td')[1].innerText
                const dataRef = item.querySelectorAll('td')[4].innerText
                const dataEnt = item.querySelectorAll('td')[5].innerText
                const status = item.querySelectorAll('td')[6].innerText
                infos.push({
                    fii,
                    categoria,
                    dataRef,
                    dataEnt,
                    status
                });

            });

            const nextPage = document.querySelector('.paginate_button.next')
            nextPage.click()
            return {
                infos
            }
        });
        
        allData.push(announcements.infos);
    }
    console.log(allData)
    // const nextPage = page.waitForSelector('.paginate_button.next', { timeout: 1000 });


}

export { getData }