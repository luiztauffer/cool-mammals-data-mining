# The Cool Mammals Project - Data Mining
This is the repository for the data mining and visualization part of the Cool Mammals project. A full blog post detailing it can be found at [Guacamole Data Science](https://luiztauffer.github.io/guacamole-data-science/posts/2019-03-16-mammals-data-mining/).

In summary, it aims to run an automatic and unsupervised algorithm to find out where a given mammal lives. It works in three steps:
1. Scraping all the pages from a Google search like 'tiger animal habitat' with [Scrapy](https://scrapy.org/). The text content of these scraped web pages is then saved locally; 
2. Countries names are identified using Named Entity Recognition functions from [SpaCy](https://spacy.io);
3. Appealing visualizations are created using [Plotly](https://plot.ly) and [Folium](https://github.com/python-visualization/folium).

For example, this is what one could find for tigers:

![tiger1](https://github.com/luiztauffer/cool-mammals-data-mining/blob/master/tiger_bars.png)


![tiger2](https://github.com/luiztauffer/cool-mammals-data-mining/blob/master/tiger_map.JPG)
