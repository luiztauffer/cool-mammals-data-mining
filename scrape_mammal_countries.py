"""
Luiz Tauffer

Scrapes the saved list of websites for each mammal and sabe a .txt file for
each page
"""
import pandas as pd
import os
import scrapy
from scrapy.crawler import CrawlerProcess


class find_countries(scrapy.Spider):
    name = "find_countries_for"
    def __init__(self, mammal, start_urls, *args, **kwargs):
        self.mammal = mammal
        self.start_urls = start_urls
        super(find_countries, self).__init__(*args, **kwargs)

    def parse(self, response):
        paragraphs = response.xpath('//p[.//text()]').extract()
        aux = response.url.replace(".","").replace(":","").replace("/","")+'.txt'
        fname = os.path.join('mammals_raw_txt', self.mammal, aux)
        dirname = os.path.dirname(fname)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(fname, "w", encoding="utf-8", errors="ignore") as text_file:
            for item in paragraphs:
                item = item.replace("<"," ").replace(">"," ").replace("/"," ")
                text_file.write("%s\n" % item)

#dataframe containing websites to search for
df = pd.read_csv('mammals_websites.csv')

mammal_list = [
    'hedgehog',
    'lion',
    'wolf',
    'fox',
    'zebra',
    'giraffe',
    'bat',
    'sloth',
    'capybara',
    'elephant',
    'rhino',
    'hippo',
    'tiger',
    'panda',
    'kangaroo',
    'koala',
]

process = CrawlerProcess()

for mammal in mammal_list:
    aux0 = df.loc[df['species']==mammal,'countries_search']
    aux1 = aux0.values.tolist()[0]
    full_list = aux1.strip("[]").replace("'", "").split(", ")
    list_urls = []
    for url in full_list:
        if "youtube" not in url: 
            list_urls.append(url)
 
    process.crawl(find_countries, mammal=mammal, start_urls=list_urls)

process.start() # the script will block here until all crawling jobs are finished



