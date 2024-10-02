import json 

import os 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Parcourir tous les fichiers json du repertoire conf.
res = {}
for i,fin in enumerate(os.listdir("conf")):
    # Filtre potentiellement les réponses
    print(fin)
    with open(os.path.join("conf",fin)) as f: 
        data = json.load(f)
    if i == 0: 
        for key in data.keys(): 
            res[key] = {data[key].lower():1} 
    else: 
        for key in res.keys():
            # On va regarder si le nouveau texte existe 
            new_entry = data[key].lower()
            found =False
            for sentence in res[key].keys(): 
                if new_entry == sentence: 
                    res[key][sentence] = res[key][sentence]  + 1 
                    found = True
            if not found: 
                res[key][new_entry] = 1

print(res)
for key in res.keys():
    plt.figure()
    wordcloud = WordCloud(
                background_color = 'white', 
                max_words = 20).generate_from_frequencies(res[key])
    plt.imshow(wordcloud)
    plt.axis("off")

plt.show()