# Set up dependencies 
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import os
from webdriver_manager.chrome import ChromeDriverManager
import time



def scrape():
    # Setup Chrome Driver for use with Splinter and initialize the browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA MARS NEWS
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
        
    # print article data
    print('-----------------')
    print(news_title)
    print(news_teaser)
    print('-----------------')

    # JP; mARS sPACE iMAGES - fEATURED iMAGE
    # Visit the JPL Mars Space Images page
    url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    # Parse the HTML on this page with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Find the link to the first displayed Image on the page and navigate to it
    image_page = soup.find('div', class_='SearchResultCard').a['href']
    full_image_page = f"https://www.jpl.nasa.gov{image_page}"
    browser.visit(full_image_page)
    time.sleep(2)

    # Parse the image page with Beautiful Soup and find the url of the full size image
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    featured_image_url = soup.find("img", class_="BaseImage").attrs["src"] 
    print(featured_image_url)

    # MARS FACTS
    # Use Pandas to visit the Mars facts page and scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = ['Fact','Detail']
    mars_facts_table = mars_df.to_html(justify='left',index=False)
    mars_df.to_html(r'C:\Users\Mthor\Bootcamp\web-scraping-challenge\Mission_to_Mars\mars_facts_tbl.html',justify='left',index=False)
    print(mars_df)

    # MARS HEMISPHERES
    # Visit the  USGS Astrogeology site and get titles of and links to Hemisphere image pages
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)

    # Parse the HTML on this page with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Retrieve the parent divs for all items
    items = soup.find_all('div', class_='item')

    # loop over results to get Hemisphere image info
    link_list = []
    title_list = []
    for item in items:
        # scrape the image title and link 
        link = item.find('a', class_='itemLink').attrs["href"] 
        title = item.find('h3').text
        link_list.append(link)
        title_list.append(title)

    # Iterate through the list of hemisphere image links and navigate to each individual page to scrape the image url
    image_list = []
    for item in link_list:
    
        #Navigate to the hemisphere image page
        article_page = f"https://astrogeology.usgs.gov{item}"
        browser.visit(article_page)
        time.sleep(2)
        
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
            
        # Retrieve elements in the downloads div and get the url to the full image
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find('a').attrs["href"]
        image_list.append(image_url)
        
    # Create a list of hemisphere dictionaries
    Cerberus = {'title':title_list[0], 'img_url':image_list[0]}
    Schiaparelli = {'title':title_list[1], 'img_url':image_list[1]}
    Syrtis = {'title':title_list[2], 'img_url':image_list[2]}
    Valles = {'title':title_list[3], 'img_url':image_list[3]}
    hemisphere_image_urls = [Cerberus, Schiaparelli, Syrtis, Valles]

    # Create a dictionary containing all of my scraped Mars website data
    Mars_dict = {
        'news_title': news_title,
        'news teaser': news_teaser,
        'featured_image_url': featured_image_url,
        'mars_facts_table': str(mars_facts_table),
        'hemisphere_image_urls': hemisphere_image_urls
        }
    return(Mars_dict)

# FOR TESTING
# Mars_dict = scrape()
# print ("Dictionary of scraped Mars data contains : " +  str(Mars_dict)) 