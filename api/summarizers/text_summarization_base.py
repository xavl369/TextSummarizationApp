# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:33:21 2023

@author: assandoval

Abstract Text Summarization Base Class
"""


from abc import abstractmethod
from preprocessors.text_preprocessor import TextPreprocessor


class TextSummarizer:
    def __init__(self):
        self.text_preprocessor = TextPreprocessor()
       
        
    # Define an abstract method using the 'abstractmethod' decorator
    @abstractmethod
    def summarize(self):
        pass
    
    @abstractmethod
    def calculate_score_sentence(self):
        pass
    
    def preprocess(self, text):
        return self.text_preprocessor.preprocess(text)

