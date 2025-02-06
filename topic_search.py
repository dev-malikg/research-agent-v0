# topic_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, urlunparse, parse_qs, unquote
import time
import requests
import json
from config import BLACKLISTED_DOMAINS, SEARCH_CONFIG, SCRAPER_CONFIG

def is_pdf_url(url):
    """Check if URL points to a PDF file"""
    if url.lower().endswith('.pdf'):
        return True
        
    try:
        headers = requests.head(url, allow_redirects=True, timeout=5)
        content_type = headers.headers.get('content-type', '').lower()
        return 'application/pdf' in content_type
    except Exception:
        return False

def is_quality_source(url):
    """Check if URL is from a reputable source"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        for bad_domain in BLACKLISTED_DOMAINS:
            if domain.endswith(bad_domain):
                return False
                
        return True
        
    except Exception:
        return False

def setup_driver():
    """Set up the Chrome driver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument(f'--user-agent={SCRAPER_CONFIG["user_agent"]}')
    return webdriver.Chrome(options=chrome_options)

def extract_actual_url(ddg_redirect_url):
    """Extract final URL from DuckDuckGo redirect links"""
    try:
        parsed = urlparse(ddg_redirect_url)
        if parsed.path == '/l/':
            query = parse_qs(parsed.query)
            if 'uddg' in query:
                return unquote(query['uddg'][0])
        return ddg_redirect_url
    except:
        return ddg_redirect_url

def clean_url(url):
    """Remove tracking parameters and fragments from URL"""
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

def search_web(query, num_results=None):
    """Searches DuckDuckGo using Selenium and returns filtered results"""
    if num_results is None:
        num_results = (SEARCH_CONFIG["main_topic_results"] 
                      if "main topic" in query.lower() 
                      else SEARCH_CONFIG["keyword_results"])
    
    try:
        driver = setup_driver()
        wait = WebDriverWait(driver, SEARCH_CONFIG["search_timeout"])
        
        driver.get("https://html.duckduckgo.com/html/")
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys(query + Keys.RETURN)
        
        results_selector = "div.web-result"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, results_selector)))
        
        elements = driver.find_elements(By.CSS_SELECTOR, results_selector)
        
        results = []
        for element in elements:
            if len(results) >= num_results:
                break
            try:
                link = element.find_element(By.CSS_SELECTOR, "a.result__a")
                title = link.text.strip()
                ddg_redirect = link.get_attribute("href")
                
                raw_url = extract_actual_url(ddg_redirect)
                clean = clean_url(raw_url)
                
                if not is_quality_source(clean):
                    continue
                
                if title and clean:
                    results.append({
                        "title": title,
                        "url": clean
                    })
                    
            except Exception:
                continue
        
        output = {
            "query": query,
            "num_results": len(results),
            "results": results
        }
        
        return json.dumps(output, ensure_ascii=False, indent=2)
        
    except Exception as e:
        error_output = {
            "query": query,
            "num_results": 0,
            "results": [],
            "error": str(e)
        }
        return json.dumps(error_output, ensure_ascii=False, indent=2)
    finally:
        driver.quit()