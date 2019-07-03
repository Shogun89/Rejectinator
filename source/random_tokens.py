# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:01:21 2019

@author: Ryan Howe
"""


import re
from nltk.corpus import wordnet
import nltk
import random


def load_tokenize(my_file):
    
    data = ''
    with open(my_file, 'r') as file:
        data = file.read().replace('\n', ' ')
    tokens = nltk.word_tokenize(data)
    return tokens
    

def syn_ant(word):
    synonyms = []
    antonyms = []
    
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
                
                
    return synonyms, antonyms

def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .',  '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
         "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()

def random_syn(random_choices,tokens):

    for choice in random_choices:
    
        syns = syn_ant(tokens[choice])
        random_syn = random.choice(syns)
        if len(random_syn)  != 0 :
            random_s = random.choice(random_syn)
            tokens[choice] = random_s
    return tokens

    
    
folder_path = 'C:\\Users\\Ryan Howe\\.spyder-py3\\Rejection\\Rejection Letters'
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

save_path = 'C:\\Users\\Ryan Howe\\.spyder-py3\\Rejection\\Rejection Examples'

n = 10
for f in onlyfiles:
    rejection_name = f.split('.')[0]
    rejection_name = rejection_name+'-editted.txt'
    rejection_path = save_path +'\\'+rejection_name
    f_edit = folder_path + '\\' + f
    
    
    tokens =load_tokenize(f_edit)
    random_choices = random.sample(range(len(tokens)), 10)
    random_s = random_syn(random_choices, tokens)
    un_token = untokenize(random_s)
    
    
    file = open(rejection_path,'w')
    file.write(un_token)
    file.close()