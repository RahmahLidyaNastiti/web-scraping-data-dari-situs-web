
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

query = 'Joko Widodo'       

n_pages = 10               

for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    search = soup.find_all('div', class_ = "yuRUbf")        
    for h in search:
        #links.append(h.a.get('href'))
        #print(h.a.text)                 
        print(h.a.get('href'))           

driver.quit()

