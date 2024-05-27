from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import sys, getopt
import argparse
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
full_text=[]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', default='', help='input filename')
    parser.add_argument('-o', '--outfile', default='', help='output filename')
    return parser.parse_args()

def main(): 
    args = parse_args()
    outfile = args.outfile
    infile = args.infile

    with open (infile, 'r', encoding = 'utf-8') as f:
        content = f.read().splitlines()
    
    for u in content[:5]:
        driver.get(u)
        elems = driver.find_element('tag name', 'body').text.split('\n') #Membersihkan \n agar menjadi baris
        filter_elems = [line for line in elems if len(line.split()) >= 5]  #Memfilter baris yang memiliki 5 atau lebih kata
        full_text.append(filter_elems)
    print(full_text)

    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(str(full_text))

    #print
    driver.close()

if __name__ == "__main__":
main()
