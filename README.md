# BDAT1007 - Fast Food Restaurants in Canada Sentiment Analysis

## Installation
Follow these steps to use the scraper:
- Download Chromedrive from [here](https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/) and extract it in Scraper directory.
- Install Python packages from requirements file using conda:

        conda create --name bdat python=3.6 --file requirements.txt

**Note**: Python >= 3.6 is required.

## Usage
Follow these steps to use the application
- Update MongoDB Connection String (CONN_STRING) in the .env file
- Replace/Add the URL's of the places from Google Maps to the file scraper/urls.txt
- To scrape the reviews from the URL's, run the following within the scraper directory:

        python3 scraper.py

- To perform sentimental analysis and subjectivity analysis, run the following within the sentiment directory:

        python3 sentiment.py


