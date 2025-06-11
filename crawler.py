from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

def start_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=options)
    return driver

def scrape_quotes():
    url = 'http://quotes.toscrape.com'
    driver = start_driver()
    driver.get(url)

    time.sleep(2)

    quotes = []
    elements = driver.find_elements(By.CLASS_NAME, 'quote')

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

    driver.save_screenshot('output/screenshot.png')

    driver.quit()
    print(f'{len(quotes)} quotes saved.')

if __name__ == '__main__':
    scrape_quotes()
