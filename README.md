# web-scraping-challenge
This project uses Python, MongoDB, Flask, Splinter, Beautiful Soup, Bootstrap and Pandas to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Part I: Web Scraping
This part of the project navigates to a variety of websites using Splinter, parses the html using BeautifulSoup and saves the scraped data to a MongoDB database. The scraping was initially done in a Jupyter notebook, and then ported to a Python script. The scraped websites are:
- NASA Mars News (https://mars.nasa.gov/news/)
- JPL Mars Space Images (https://www.jpl.nasa.gov/images?search=&category=Mars)
- Space Facts (https://space-facts.com/mars/)
- Astrogeology Mars Hemisphere pages (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

It consists of:
- a local MongoDB database (mars_db)
- a Jupyter notebook (Mission_to_Mars/mission_to-mars.ipnyb) 

## Part II: MongoDB and Flask Application
This part of the project is a web application that uses Flask, HTML and PyMongo to display all of the information scraped in Part 1. It also provides a "Get latest Mars info!" button that will scrape the latest website data, update the database and display it. 

It consists of:
- a Flask app (Mission_to_Mars/app.py) with two Flask routes: 
    1.  **/** &nbsp; &nbsp;&nbsp; &nbsp;--->Mission to Mars Home page (see image below)
    2. **/scrape** &nbsp; &nbsp;-->executes web scraping script
- a Python script (Mission_to_Mars/scrape_mars.py)
- an HTML file (Mission_to_Mars/templates/index.html)
- various Bootstrap CSS and Jquery files, and a background image  (Mission_to_Mars/static)
- several screenshots of the final web page in Mission_to_Mars/ 
    - Bottom-screenshot.jpg, Top-screenshot.jpg and Single-screenshot.jpg

## Getting Started

Follow these steps to run this web application on your machine.

### Prerequisites

You will need BeautifulSoup, Splinter, ChromeDriverManager, Flask, Python, Pandas, PyMongo, MongoDB, Jupyter Notebook and the Chrome browser. 

### Steps to follow

1- Ensure all of the software listed above is installed on your machine<br>
2- Start up and/or connect to a local MongoDB server and using Compass or the command line create a new database called "mars_db".<br>
```
> use mars_db
```
3- Create a collection in "mars_db" called "mars_info"<br>
```
> mars_db.createCollection(mars_info)
```
4- Run app.py from the terminal<br>
5- Open your Chrome browser and enter this url 
```
http://127.0.0.1:5000/
```
6- To scrape the latest Mars data press the button that says:

```
Get Latest Mars Info!
```
![Mission to Mars Website Image: ](https://github.com/MThorpester/web-scraping-challenge/blob/main/Mission_to_Mars/Single-screenshot.jpg)