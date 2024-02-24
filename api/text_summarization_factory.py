# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:00:56 2023

@author: assandoval

Text Summarization Factory
"""

from enum import Enum, auto

from summarizers import Bert, FrequencyBased, CosineSimilarity, GPT, LSTM, Luhn, Edmundson, KlSum, LexRank, Lsa, SumyLuhn

class TextSummarizers(Enum):
    Bert = auto()
    FrequencyBased = auto()
    CosineSimilarity = auto()
    GPT = auto()
    LSTM = auto()
    Luhn = auto()
    Edmundson = auto()
    KlSum = auto()
    LexRank = auto()
    Lsa = auto()
    SumyLuhn = auto()


class TextSummarizerAbtractFactory():
    
    availableSummarizers = TextSummarizers    
    factories = []
    initialized = False
        
    def __init__(self):
        self.create_factories()
       
    def create_summarizer(self, method):
        return self.factories[method - 1][1];
    
    def create_factories(self):
        for d in self.availableSummarizers:
            name = d.name[0] + d.name[1:]
            factory_name = name
            factory_instance = eval(factory_name)()
            self.factories.append((name, factory_instance))
        
class TextSummarizerFactory():
    
    def __init__(self, method):
        
        self.method = TextSummarizers[method]
        abstract_factory = TextSummarizerAbtractFactory();
        self.summarizer = abstract_factory.create_summarizer(self.method.value)
        
    def summarize(self, p):
       
        if self.method in [TextSummarizers.Bert, TextSummarizers.LSTM, TextSummarizers.GPT]:
            return self.summarizer.summarize(p.text)
        
        if self.method in [TextSummarizers.FrequencyBased, TextSummarizers.CosineSimilarity, TextSummarizers.SumyLuhn, TextSummarizers.Edmundson,
                           TextSummarizers.KlSum, TextSummarizers.LexRank, TextSummarizers.Lsa ]:
            return self.summarizer.summarize(p.text, p.n_sentences, p.percentage)
        
        if self.method == TextSummarizers.Luhn:
            return self.summarizer.summarize(p.text, p.n_sentences, p.percentage, p.top_n_words, p.distance)
    
    
    @staticmethod
    def create_params(text, n_sentences, percentage = 0.5, top_n_words = 150, distance = 1):
        
        DynamicClass = type("DynamicClass", (object,),  {
            "text": text,
            "n_sentences": n_sentences,
            "percentage": percentage,
            "top_n_words": top_n_words,
            "distance": distance
        })
        
        return DynamicClass()
    