# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:37:54 2024

@author: LCC Abraham Saul Sandoval Meneses

Sumy - Luhn Algorithm

1.- It is one of the earliest suggested algorithm by the famous IBM researcher it was named after. 
2.- It scores sentences based on frequency of the most important words.

https://miso-belica.github.io/sumy/
https://miso-belica.github.io/sumy/summarizators.html


Heuristic method - the simplest real-world algorithm. 
It’s the first one known and it’s based on the assumption that the most important sentences are those with the most significant words. 
The significant words are those which are more often in the text but at the same time, they don’t belong among stop-words. 
That’s why if you want to use this one you need a list of stop-words for your language. 
Without it, it would probably produce really bad results.
"""


import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from summarizers.text_summarization_base import TextSummarizer

class SumyLuhn(TextSummarizer):
  
    def __init__(self):
        super().__init__()
        
    def summarize(self, text, number_of_sentences, percentage = 0):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        if percentage > 0:
            number_of_sentences = int(len(original_sentences) * percentage)
       
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        summarizer = LuhnSummarizer()
        summary = summarizer(parser.document, number_of_sentences)
        
        best_sentences = [str(sentence) for sentence in summary]
       
        return original_sentences, best_sentences, None
    
# if __name__ == "__main__":
#     text = """Artificial intelligence is human like intelligence. 
#                         It is the study of intelligent artificial agents. 
#                         Science and engineering to produce intelligent machines. 
#                         Solve problems and have intelligence. 
#                         Related to intelligent behavior. 
#                         Developing of reasoning machines. 
#                         Learn from mistakes and successes. 
#                         Artificial intelligence is related to reasoning in everyday situations."""
                        
#     sumy_luhn_summarization = SumyLuhn()
#     sentence_list, best_sentences, score_sentences = sumy_luhn_summarization.summarize(text, 0, 0.5)   