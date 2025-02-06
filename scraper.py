# scraper.py
from bs4 import BeautifulSoup
import requests
from config import SCRAPER_CONFIG

def scrape(url):
    """Scrape content from a webpage with configured settings"""
    headers = {"User-Agent": SCRAPER_CONFIG["user_agent"]}
    
    for attempt in range(SCRAPER_CONFIG["max_retries"]):
        try:
            response = requests.get(
                url, 
                headers=headers, 
                timeout=SCRAPER_CONFIG["timeout"]
            )
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            paras = soup.find_all("p")
            text_content = "\n".join(para.text for para in paras)
            
            return text_content
            
        except Exception as e:
            if attempt == SCRAPER_CONFIG["max_retries"] - 1:
                raise e
            continue