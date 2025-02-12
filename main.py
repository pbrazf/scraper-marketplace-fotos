from selenium_driverless import webdriver
from bs4 import BeautifulSoup
import asyncio, requests

async def iniciar_driver():
    '''Inicia o WebDriver e espera o login manual.'''
    driver = await webdriver.Chrome().__aenter__()
    await driver.set_window_size(1920, 1080)
    await driver.get('https://shopee.com.br/buyer/login', wait_load=True)
    input('Faça login (Talvez resolver o captcha de login), espere a tela carregar e pressione Enter...')
    print()
    return driver

async def acessar_pagina(driver, url, tempo_espera):
    '''Acessa uma URL e retorna o código-fonte.'''
    await driver.get(url, wait_load=True)
        
    # Aguarda até que esteja completamente carregado
    await asyncio.sleep(tempo_espera)
    return await driver.page_source

async def salvar_imagem(codigo_fonte, caminho):
    '''Extrai e salva a imagem do produto.'''
    sopa = BeautifulSoup(codigo_fonte, 'html.parser')
    meta_imagem = sopa.find('meta', property='og:image')
    if not meta_imagem:
        return False
    
    # Baixa a imagem
    url_imagem = meta_imagem['content']
    resposta = requests.get(url_imagem, stream=True)
    if resposta.status_code == 200:
        with open(f'{caminho}.jpg', 'wb') as arquivo:
            for bloco in resposta.iter_content(1024):
                arquivo.write(bloco)
        return True
    return False

async def scraper_imagem(produtos):
    '''Executa o scraping e salva imagens dos produtos.'''
    driver = await iniciar_driver()
    
    for caminho, url in produtos.items():
        print(f'Buscando imagem do produto: {caminho}')
        for _ in range(3):  # Máximo de 3 tentativas
            print(f'    Tentativa {_ + 1}...')
            codigo_fonte = await acessar_pagina(driver, url, tempo_espera = 5 if 'shopee' in url.lower() else 2)
            if await salvar_imagem(codigo_fonte, caminho):
                print(f'    Imagem salva com sucesso!')
                break
            await asyncio.sleep(5)
        print()
        # Aguarda um tempo de 2 segundos
        await asyncio.sleep(2)

    await asyncio.sleep(3)
    await driver.quit()

# ------------------------------------------------------------------------------
# Exemplo de uso:
asyncio.run(scraper_imagem({
        'parafusadeira': 'https://shopee.com.br/kit-Parafusadeira-furadeira-45-P%C3%A7s-%C3%80-Bateria-Carregador-Usb-Oferta-especial-i.828971089.22097287831',
        'ram': 'https://pt.aliexpress.com/item/1005005123905984.html',
        'serra': 'https://shopee.com.br/Moto-Serra-El%C3%A9trica-1200W-12-Polegadas-Com-Duas-Baterias-48V-completa-super-forte-i.828971089.20499194753',
        'fone': 'https://pt.aliexpress.com/item/1005007187792794.html'
    }))
