from urllib import request
from jotform import *
import pandas as pd
import numpy as np
import requests
import json
from tqdm import tqdm
import logging as log
from nltk.tokenize import ToktokTokenizer
import nltk
import csv
import codecs
from io import StringIO
import gcld3
from bs4 import BeautifulSoup
import unicodedata
import re 
import string
import cld3


import os
from dotenv import load_dotenv

load_dotenv()


typeArray = ["control_text","control_textarea","control_textbox","control_fullname","control_head"]


def getInformation(formID):
  textArray = []

  pageTitleFlag = None
  contentFlag = None
  property = requests.get(f"https://api.jotform.com/form/{formID}/properties?apiKey={os.getenv('JOTFORM_APIKEY')}")
  try:
    pageTitle = str(property.json()['content']['pagetitle'])
  except:
    pageTitleFlag = True
          
  question = requests.get(f"https://api.jotform.com/form/{formID}/questions?apiKey={os.getenv('JOTFORM_APIKEY')}") 
  try:       
    for k in question.json()['content'].values():
      if(k['type'] in typeArray):
        textArray.append(str(k['text']))
  except:
    contentFlag = True
                       
  if(pageTitleFlag == True and contentFlag == True):
    print(f"{formID} -- Not found pageTitle and content")
  elif(pageTitleFlag == True):
    rawData = {"Form_ID":formID,"Page_Title":pageTitle,"Raw_Text":". ".join(textArray)}
    print(f"{formID} -- Not found pageTitle")
  elif(contentFlag == True):
    rawData = {"Form_ID":formID,"Page_Title":pageTitle,"Raw_Text":". ".join(textArray)}
    print(f"{formID} -- Not found content")
  else:
    rawData = {"Form_ID":formID,"Page_Title":pageTitle,"Raw_Text":". ".join(textArray)}
            
  return rawData



## TODO: init functions
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')



def remove_html_tags(text):
    return BeautifulSoup(text, 'html.parser').get_text()
################
def remove_accented_chars(text):
    new_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return new_text
################
def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    return re.sub(pat, '', text)
################
def remove_numbers(text):
    # define the pattern to keep
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    return re.sub(pattern, '', text)
################
def remove_punctuation(text):
    text = ''.join([c for c in text if c not in string.punctuation])
    return text
################
def to_df(file):
    data = file.file
    data = csv.reader(codecs.iterdecode(data,'utf-8'), delimiter=',')
    header = data.__next__()
    df = pd.DataFrame(data, columns=header)
    return df


stopword_list.remove('not') # because it indicate that all sentence is negative 
def remove_stopwords(text):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    t = [token for token in tokens if token.lower() not in stopword_list]
    text = ' '.join(t)    
    return text
################
def remove_extra_whitespace_tabs(text):
    #pattern = r'^\s+$|\s+$'
    pattern = r'^\s*|\s\s*'
    return re.sub(pattern, ' ', text).strip()
################
def to_lowercase(text):
    return text.lower()
################
def get_language(text):
    lang =cld3.get_language(text)
        
    if(lang is None):
        return "other"
    
    if(lang.probability > 0.499):
        try:
            return lang.language
        except:
            
            return "other"
    else:
        return "other"





def all_preprocessing_stages(text):
    text = remove_html_tags(text)
    text = remove_accented_chars(text)
    text = remove_special_characters(text)
    text = remove_special_characters(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_extra_whitespace_tabs(text)
    return to_lowercase(text) 
  
  
  
stopword_list = nltk.corpus.stopwords.words(['english',"spanish", "french", "portuguese",
                                             "german", "italian", "indonesian",
                                             "norwegian", "dutch", 
                                             "danish", "turkish"])
def remove_stopwords(text):
    # convert sentence into token of words
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    # check in lowercase 
    t = [token for token in tokens if token.lower() not in stopword_list]
    text = ' '.join(t)    
    return text

 

                    
     