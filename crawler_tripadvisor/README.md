# Tripadvisor crawler

Beacuse of the complexity of the data gathering, this area should have its own readme.

## Contents
This project has two spiders:
- [`tripadvisor`](cr_tripadvisor/spiders/tripadvisor.py) -> gets all the restaurants listed on tripadvisor's madrid site.
- [`restaurants`](cr_tripadvisor/spiders/restaurants.py) -> enriches the scraped restaurant accesing the scraped links from tripadvisor.

## Usage

In order to start a new scrapy project, this is how to set it up:

> scrapy startproject tutorial

First step is to obtain the restaurant list published on tripadvisor. The recommendation is to scrape the data on `.json` format. The name of the file it's needed to be specified as argument and also the main url of the city / territory you want to scrape.

> scrapy crawl tripadvisor -a url='https://www.tripadvisor.es/Restaurants-g187514-Madrid.html#EATERY_LIST_CONTENTS' -o your-file-name.json

Next, this crawler will access each scraped link from the previous spider and gather the required information for each restaurant. In this case, the result of the previos scraping is the function argument (as json) and it will enrich the previous data with the one accessible on the restaurant links.

> scrapy crawl restaurants -a json=your-file-name.json -o you-enriched-file-name.json

## Acknowledgements

This crawler was based on the one developed by [@carloalbe](https://github.com/carloalbe/).