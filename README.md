# Scraper de Imagens de Produtos (Shopee & AliExpress)

Este projeto é um scraper assíncrono desenvolvido em Python que utiliza Selenium Driverless para coletar a primeira imagem de produtos em sites como Shopee e AliExpress. Ele foi desenvolvido como um trabalho freelance e visa contornar captchas difíceis encontrados nesses sites.

🚀 Tecnologias Utilizadas

Python
Selenium Driverless (para navegação sem exibição de navegador)
BeautifulSoup (para extração de dados HTML)
Requests (para baixar imagens)
Asyncio (para execução assíncrona)

🛠️ Como Usar

1. Instale as dependências
Certifique-se de ter Python instalado e execute:
`pip install selenium-driverless beautifulsoup4 requests`

3. Execute o script
`python scraper.py`
Durante a execução, o script irá solicitar que você faça login na Shopee manualmente antes de iniciar o scraping.

4. Estrutura do Código

iniciar_driver() → Inicia o navegador e aguarda o login manual.
acessar_pagina(driver, url, tempo_espera) → Acessa a página e retorna o HTML.
salvar_imagem(codigo_fonte, caminho) → Extrai a URL da imagem e salva localmente.
scraper_imagem(produtos) → Gerencia o processo para vários produtos.

🔥 Desafios Resolvidos

✅ Utiliza Selenium Driverless para contornar captchas complexos da Shopee.
✅ Implementa scraping assíncrono para maior eficiência.
✅ Faz o download da primeira imagem do produto de forma automatizada.

📌 Melhorias Futuras

Automatizar o login na Shopee sem necessidade de intervenção manual.
Implementar suporte para mais sites de e-commerce.

📌 Autor: Pedro
