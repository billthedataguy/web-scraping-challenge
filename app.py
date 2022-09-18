# Flask app

# Dependencies 

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Instantiate flask app

app = Flask(__name__)

# Instantiate MongoDB via PyMongo
 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Flask routes

@app.route("/")
def index():

    # Get most recent data in the MongoDB database

    fetch_data = mongo.db.mars.find_one()        

    # Serve the data up through a Jinja2 template that uses Bootstrap 

    return render_template("index.html", mars_data=fetch_data)

@app.route("/scrape")
def scrape():

    # Perform the web scraping
    
    mars_data = scrape_mars.scrape()

    # Update MongoDB database

    mongo.db.mars.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect to the index route

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)