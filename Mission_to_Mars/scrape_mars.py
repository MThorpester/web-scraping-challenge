# Set up dependencies 
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import os
from webdriver_manager.chrome import ChromeDriverManager
import time


# def scrape():
# Setup Chrome Driver for use with Splinter and initialize the browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Navigate to the URL of the NASA Mars News page to scrape it
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(2)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Scrape the article title and the teaser text from the first list_text class div element on the page
article = soup.find('div', class_='list_text')
news_title = article.find('div', class_='content_title').text
news_teaser = article.find('div', class_='article_teaser_body').text
article_date = article.find('div', class_='list_date').text
    
# print article data
print('-----------------')
print(article_date)
print(news_title)
print(news_teaser)
print('-----------------')


