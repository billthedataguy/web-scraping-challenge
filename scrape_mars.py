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
    
    mars_dict["news_title"] = soup.find("div", class_="content_title").text
    mars_dict["news_paragraph"] = soup.find("div", class_="article_teaser_body").text
    
    #############################
    ## GET FEATURED MARS IMAGE ##
    #############################

    url2 = 'https://spaceimages-mars.com/'

    browser.visit(url2)

    time.sleep(2) 
    
    browser.links.find_by_partial_text('FULL IMAGE').click()
    
    html = browser.html    
    soup = bs(html, "html.parser")

    image_rel_url = soup.find("img", class_="fancybox-image")["src"]    
    image_featured_url = f"{url2}{image_rel_url}"
    
    mars_dict["image_featured_url"] = image_featured_url
    
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

    html_table = df.to_html(classes="table table-striped", index=False)

    mars_dict["html_table"] = html_table

    ######################################
    ## GET MARS HEMISPHERES IMAGES ##
    ######################################

    url4 = 'https://marshemispheres.com/'

    browser.visit(url4)    

    html = browser.html

    soup = bs(html, "html.parser")

    # iterate over image_tags and collect img_titles

    image_tags = soup.find_all("img", class_="thumb")

    img_titles = []

    for tag in image_tags:
        
        img_titles.append(tag["alt"].replace(" thumbnail", ""))

    links_found = browser.find_by_css('h3').links.find_by_partial_text('Hemisphere Enhanced')

    # iterate over links_found and collect jpg_img_urls

    links_found = browser.find_by_css('h3').links.find_by_partial_text('Hemisphere Enhanced')

    jpg_img_urls = []

    for link in links_found:
        
        img_link = link["href"]    
            
        browser.visit(img_link)

        time.sleep(2)   

        html = browser.html
        soup = bs(html, 'html.parser')
        
        img_tag = soup.find("img", class_="wide-image")    
        
        img_url = f'{url4}{img_tag["src"]}'         
        
        jpg_img_urls.append(img_url)
        
        browser.back()
        
        time.sleep(2)
        
    print("Scrape completed!")

    browser.quit()

    photo_data = list(zip(img_titles, jpg_img_urls))
    
    mars_dict["photo_data"] = photo_data  
    
    return mars_dict