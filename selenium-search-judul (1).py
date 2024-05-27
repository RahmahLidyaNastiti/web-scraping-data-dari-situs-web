from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

# Query to obtain links
query = 'Joko Widodo'       

n_pages = 2                

for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 2) 
    driver.get(url)
    
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "yuRUbf")))
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
 
    search = soup.find_all('div', class_ = "yuRUbf")       
    for h in search:
        print(h.a.text)                
        print(h.a.get('href'))          
driver.quit()