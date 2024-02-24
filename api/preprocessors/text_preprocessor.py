# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:37:11 2023

@author: assandoval

Text Preprocessor
"""

import re 
import nltk 
import string
import pickle
from bs4 import BeautifulSoup
#nltk.download('punkt')
#nltk.download('stopwords')

import os



class TextPreprocessor:
    
    def __init__(self):
        self.stop_words_en = self.__load_stop_words()
        
    def __load_stop_words(self):
        current_directory = os.getcwd()
        with open(f'{current_directory}\\preprocessors\\stopwords_en.pickle', 'rb') as file:
            stop_words_en = pickle.load(file)
            
        return stop_words_en
    
    def preprocess(self, text):
        preprocessed_text = re.sub(r'\s+', ' ', text) 
        preprocessed_text = preprocessed_text.lower()  
        tokens = [token for token in nltk.word_tokenize(preprocessed_text)] 
        tokens = [word for word in tokens if word not in self.stop_words_en and word not in string.punctuation] 
        preprocessed_text = ' '.join(element for element in tokens) 
        
        return preprocessed_text
    
    def clean_tweet(tweet):
        tweet = BeautifulSoup(tweet, "lxml").get_text()
        # Removing the @
        tweet = re.sub(r"@[A-Za-z0-9]+", ' ', tweet)
        # Removing the URL links
        tweet = re.sub(r"https?://[A-Za-z0-9./]+", ' ', tweet)
        # Keeping only letters
        tweet = re.sub(r"[^a-zA-Z.!?']", ' ', tweet)
        # Removing additional whitespaces
        tweet = re.sub(r" +", ' ', tweet)
        
        if tweet == ' ':
            return ''
        
        if tweet[0] == ' ':
            tweet = tweet[1:]
            
        if tweet[-1] == ' ':
            tweet = tweet[:-1]
            
        return tweet
        



















