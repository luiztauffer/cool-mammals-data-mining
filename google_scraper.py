"""
Author:  Luiz

Using google search scraper by https://github.com/MarioVilas/googlesearch
"""
from googlesearch import search, get_random_user_agent
import pandas as pd
import time

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

df = pd.DataFrame(data=mammal_list, columns=['species'])                                         
df['countries_search'] = ''
df['countries_search'] = df['countries_search'].astype(object)

#Search 100 Google results for each species
for mammal in mammal_list:
    all_urls = []
    print('searching '+mammal)
    results = search(mammal+" animal habitat", num=50, stop=200, pause=60., 
                     only_standard=True, user_agent=get_random_user_agent())
    [all_urls.append(i) for i in results]
            
    df.at[df['species']==mammal,'countries_search'] = [all_urls]
    df.to_csv('mammals_websites.csv', index=False)
    time.sleep(60)
    
    
#Add conservation websites
df['conservation_search'] = ''
df['conservation_search'] = df['conservation_search'].astype(object)

df.at[df['species']=='hedgehog','conservation_search'] = 'https://www.britishhedgehogs.org.uk/'
df.at[df['species']=='lion','conservation_search'] = 'https://www.conservationafrica.net/our-projects/lion-conservation-projects/'
df.at[df['species']=='wolf','conservation_search'] = 'https://nywolf.org/'
df.at[df['species']=='fox','conservation_search'] = 'http://www.nfws.org.uk/'
df.at[df['species']=='zebra','conservation_search'] = 'http://www.grevyszebratrust.org/'
df.at[df['species']=='giraffe','conservation_search'] = 'https://giraffeconservation.org/'
df.at[df['species']=='bat','conservation_search'] = 'http://www.batcon.org/'
df.at[df['species']=='sloth','conservation_search'] = 'https://slothconservation.com/'
df.at[df['species']=='capybara','conservation_search'] = 'https://www.worldlandtrust.org/species/mammals/capybara/'
df.at[df['species']=='elephant','conservation_search'] = 'https://www.sheldrickwildlifetrust.org/'
df.at[df['species']=='rhino','conservation_search'] = 'https://www.savetherhino.org/'
df.at[df['species']=='hippo','conservation_search'] = 'http://www.gorongosa.org/explore-park/wildlife/gorongosas-hippos/hippo-conservation'
df.at[df['species']=='tiger','conservation_search'] = 'https://www.wcs.org/our-work/species/tigers'
df.at[df['species']=='panda','conservation_search'] = 'https://www.pandasinternational.org/'
df.at[df['species']=='kangaroo','conservation_search'] = 'http://www.australiansocietyforkangaroos.com/'
df.at[df['species']=='koala','conservation_search'] = 'https://www.savethekoala.com/'

df.to_csv('mammals_websites.csv', index=False)









