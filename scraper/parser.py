import pandas as pd
import os
from scraper.utils import setup_logger

logger = setup_logger()

def display_with_pandas():
    output_path = os.path.join('output', 'quotes.csv')

    if not os.path.exists(output_path):
        logger.warning(f"O arquivo {output_path} não foi encontrado.")
        return

    try:
        df = pd.read_csv(output_path)

        pd.set_option('display.max_colwidth', None)
        logger.info("Exibindo as 5 primeiras citações extraídas:\n")
        print(df.head(5).to_string(index=False))
    except Exception as e:
        logger.exception(f"Erro ao tentar ler o arquivo CSV: {e}")

