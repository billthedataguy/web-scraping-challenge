from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
   
    mars_dict = {}

    ###################
    ## GET MARS NEWS ##
    ###################
    
    url1 = 'https://redplanetscience.com/'
    
    browser.visit(url1)   

    time.sleep(2)    

    html = browser.html    

    soup = bs(html, "html.parser")
    
    mars_dict["title"] = soup.find("div", class_="content_title").text
    mars_dict["paragraph"] = soup.find("div", class_="article_teaser_body").text
    
    #############################
    ## GET FEATURED MARS IMAGE ##
    #############################

    url2 = 'https://spaceimages-mars.com/'

    browser.visit(url2)

    time.sleep(2)    

    html = browser.html    
    
    browser.links.find_by_partial_text('FULL IMAGE').click()

    image_rel_url = soup.find("img", class_="fancybox-image")["src"]    
    featured_image_url = f"{url2}{image_rel_url}"

    
    mars_dict["featured_image_url"] = featured_image_url
    
    ##########################
    ## GET MARS FACTS TABLE ##
    ##########################

    url3 = "https://galaxyfacts-mars.com/"

    browser.visit(url3)

    time.sleep(2)    

    tables = pd.read_html(url3)

    df = tables[1]

    df = df.rename(columns={0:"Characteristic", 1:"Data"})

    df["Characteristic"] =  df["Characteristic"].str.rstrip(":")

    html_table = df.to_html()

    html_table.replace('\n', '') 

    mars_dict["html_table"] = html_table

    ######################################
    ## GET MARS HEMISPHERES .TIF IMAGES ##
    ######################################

    url4 = 'https://marshemispheres.com/'

    browser.visit(url4)    

    html = browser.html

    soup = bs(html, "html.parser")

    image_tags = soup.find_all("img", class_="thumb")

    # iterate over image_tags to get tif_title for each img

    tif_title = image_tags[0]["alt"].replace(" Enhanced thumbnail", "")
    tif_title

    links_found = browser.find_by_css('h3').links.find_by_partial_text('Hemisphere Enhanced')
    links_found

    for link in links_found:
        img_link = link["href"]
        print(img_link)

    browser.visit(links_found[0]["href"])

    time.sleep(2)    

    html = browser.html
    soup = bs(html, 'html.parser')

    downloads_tags = soup.find("div", class_="downloads")

    img_tags = downloads_tags.find_all("a")

    # iterate over img_tags to get tif_url for each img

    tif_url = f'{url4}{img_tags[1]["href"]}'
    tif_url

    mars_dict["tif_title"] = tif_title
    mars_dict["tif_url"] = tif_url

    browser.quit()

    return mars_dict