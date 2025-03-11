from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def initialize_webdriver():
    driver = webdriver.Chrome()
    return driver

def scrape_quotes(driver):
    url = 'http://quotes.toscrape.com'
    driver.get(url)
    
    quotes = []
    authors = []
    tags = []
    
    while True:
        quote_elements = driver.find_elements(By.CLASS_NAME, 'quote')
        for quote_element in quote_elements:
            text = quote_element.find_element(By.CLASS_NAME, 'text').text
            author = quote_element.find_element(By.CLASS_NAME, 'author').text
            tag_elements = quote_element.find_elements(By.CLASS_NAME, 'tag')
            quote_tags = [tag.text for tag in tag_elements]
            
            quotes.append(text)
            authors.append(author)
            tags.append(quote_tags)
        
        try:
            next_button = driver.find_element(By.CLASS_NAME, 'next')
            next_button.click()
            time.sleep(2)
        except:
            break
    
    return quotes, authors, tags

def main():
    driver = initialize_webdriver()
    quotes, authors, tags = scrape_quotes(driver)
    
    for i in range(len(quotes)):
        print(f'Quote: {quotes[i]}')
        print(f'Author: {authors[i]}')
        print(f'Tags: {", ".join(tags[i])}')
        print('-' * 80)
    
    driver.quit()

if __name__ == '__main__':
    main()
