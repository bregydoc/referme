from enum import auto
from typing import List

import autoscraper


def train_scraper() -> autoscraper.AutoScraper:
    scraper = autoscraper.AutoScraper()

    return scraper


def extract_dois_of_page(scraper: autoscraper.AutoScraper, page_url: str) -> List[str]:
    # scraper.build(page_url, )
    return ["unknown", "unknown"]
