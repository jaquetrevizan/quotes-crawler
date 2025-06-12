from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from scraper.parser import display_with_pandas
import pandas as pd
import time
import os

from scraper.utils import setup_logger

logger = setup_logger()

def start_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    logger.debug("Inicializando o Chrome WebDriver com opções headless.")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_quotes():
    url = 'http://quotes.toscrape.com'
    logger.info(f"Iniciando scraping em: {url}")

    try:
        driver = start_driver()
        driver.get(url)
        logger.debug("Página carregada com sucesso.")
        
        time.sleep(2)

        quotes = []
        elements = driver.find_elements(By.CLASS_NAME, 'quote')

        logger.debug(f"Encontrados {len(elements)} elementos com classe 'quote'.")

        for el in elements:
            text = el.find_element(By.CLASS_NAME, 'text').text
            author = el.find_element(By.CLASS_NAME, 'author').text
            tags = [tag.text for tag in el.find_elements(By.CLASS_NAME, 'tag')]

            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })

        os.makedirs('output', exist_ok=True)

        df = pd.DataFrame(quotes)
        df.to_csv('output/quotes.csv', index=False, encoding='utf-8')
        logger.success("Arquivo CSV salvo com sucesso em output/quotes.csv.")

        driver.save_screenshot('output/screenshot.png')
        logger.success("Screenshot salva em output/screenshot.png.")

        logger.info(f"{len(quotes)} citações extraídas com sucesso.")
    except Exception as e:
        logger.exception(f"Ocorreu um erro durante o scraping: {e}")
    finally:
        driver.quit()
        logger.debug("Driver encerrado.")

def run_crawler():
    scrape_quotes()
    display_with_pandas()
