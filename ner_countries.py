'''
Luiz Tauffer

Named Entity Recognition to find Countries for mammals
'''
import spacy
import os 
import operator
import pandas as pd

#nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_lg')

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
df['country_counts'] = ''
df['country_counts'] = df['country_counts'].astype(object)
df['number_results'] = 0

for mammal in mammal_list:
    print('Running NER for:', mammal)
    all_files = os.listdir(os.path.join('mammals_raw_txt', mammal))
    all_sets = []
    for fname in all_files:
        file_path = os.path.join('mammals_raw_txt', mammal, fname)
        with open(file_path, 'r', encoding="utf-8", errors="ignore") as myfile:
            data = myfile.read().replace('\n',' ').replace('type',' ').replace('=',' ')
        data = data[0:50000]   #protect from memory error
        doc = nlp(data)
        
        curr_ents = []
        for X in doc.ents:
            if X.label_ == 'GPE':
                ent_txt = (X.text).lower()#replace(" ", "")
                curr_ents.append(ent_txt)
        
        #Gets unique values in lists
        myset = set(curr_ents)
        all_sets = all_sets + list(myset)
        
    #Counts number of occurrences  
    wrd_cnt = {}    
    for wrd in all_sets:
        if wrd not in wrd_cnt:
            wrd_cnt[wrd] = 1
        else: wrd_cnt[wrd] += 1
    
    #Sorts by number of occurrences    
    sorted_x = sorted(wrd_cnt.items(), key=operator.itemgetter(1), reverse=True)    
    df.at[df['species']==mammal,'country_counts'] = [sorted_x]
    
    #Number of scraped files
    df.at[df['species']==mammal,'number_results'] = len(all_files)

    df.to_csv('mammals_country_counts.csv', index=False)