# web-scraping-challenge

## William Vann
## Homework 12 - **Mission to Mars**

<br>

# Part 1: Scraping


**This project demonstrates web scraping 4 different Mars-themed websites with BeautifulSoup and Splinter, as follows:**


1. [https://redplanetscience.com/](https://redplanetscience.com/)
        
        Scrape the latest Mars news title and accompanying news paragraph.

2. [https://spaceimages-mars.com/](https://spaceimages-mars.com/)

        Scrape a featured Mars image url.

3. [https://galaxyfacts-mars.com/](https://galaxyfacts-mars.com/)

        Scrape an html table with Mars facts.

4. [https://marshemispheres.com/](https://marshemispheres.com/)

        Scrape high-resolution Mars hemisphere images with their titles.


# Part 2: MongoDB and Flask Application

**The web-scraped artefacts from Part 1 are stored in a MongoDB and served up via a Bootstrap-responsive Flask html template with customized CSS.**  

### Files in this Repo

1. [app.py](app.py)

        Flask app with index route and scrape route.

2. [scrape_mars.py](scrape_mars.py)

        Contains scrape() function which is called by scrape route in app.py.

3. [mission_to_mars.ipynb](mission_to_mars.ipynb)

        Jupyter notebook containing all scraping and analysis logic.

4. [templates/index.html](templates/index.html)

        Bootstrap-responsive Jinja2 template with all of the web-scraped Mars data served by Flask app.

5. [static/css/style.css](static/css/style.css)

        Customized CSS added over the Bootstrap CSS. 

6. [screenshot_1.jpg](screenshot_1.jpg)

        Screenshot of Flask app on large display.

7. [screenshot_2.jpg](screenshot_2.jpg)

        Screenshot of Flask app on mobile display.

8. [screenshot_3.jpg](screenshot_3.jpg) 

        Screenshot of automated splinter browser running.




