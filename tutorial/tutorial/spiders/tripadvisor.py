import scrapy
import re 

class tripadvisor(scrapy.Spider):

   #the name of the spider
   name = 'tripadvisor'

   #these are the urls that we will start scraping
   allowed_domains = ['tripadvisor.es']
   start_urls = ['https://www.tripadvisor.es/Restaurants-g187514-Madrid.html#EATERY_LIST_CONTENTS']

   def parse(self, response):
        prod_class = 'roxNU.Vt.o'
        prod_name = 'Lwqic.Cj.b'
        prod_object = 'hBcUX.XFrjQ.mIBqD'
        products = response.css(f'div.{prod_class}')
        # /html/body/div[4]/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div/div[5]/div[3]/div[5]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div
        # /html/body/div[4]/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div/div[5]/div[3]/div[5]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[1]/div
        for product in products:
            #here we put the data returned into the format we want to output for our csv or json file
            print(product)
            yield {
                'name_clean' : product.css(f'span.Lwqic.Cj.b::text').get(),#aun no
                'name': product.css(f'a.{prod_name}').get(),
                'price' : product.css(f'span.{prod_object}').get(), #.replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
                'price_clean' : product.css('span.tqpbe').get(),
                'reviews' : product.css('span.IiChw').get(),
                'rating' : product.css('span.GmcgY').get(), #aun no
                'url' : product.css(f'a.{prod_name}').attrib['href'],
            }

        #next_page = response.css('[rel="next"] ::attr(href)').get()

        #if next_page is not None:
        #    next_page_url = 'https://www.chocolate.co.uk' + next_page
        #    yield response.follow(next_page_url, callback=self.parse)

        next_page = response.css('a.nav.next.rndBtn.ui_button.primary.taLnk').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)