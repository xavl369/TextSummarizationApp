# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:47:24 2024

@author: abrah


Sumy - Edmundson

Heuristic method with previous statistic research - the enhancement of the Luhn method mentioned previously. 
Edmundson added 3 more heuristics to the method to measure the importance of the sentences. 
He finds so-called pragmatic words, the words that are in headings and the position of the extracted terms. 
Therefore this method has 4 sub-methods and the proper combination of them results in the Edmundson method. 
The important part is that this method is the most language-dependent because it needs the list of bonus words 
and stigma words except for the stop-words (called the null words here). 
If you are serious about the summary you should read how Edmundson mined these words from the corpus in the original paper. 
"""

import nltk
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.utils import get_stop_words
from summarizers.text_summarization_base import TextSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


class Edmundson(TextSummarizer):
  
    def __init__(self):
        super().__init__()
        
    def summarize(self, text, number_of_sentences, percentage = 0):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        if percentage > 0:
            number_of_sentences = int(len(original_sentences) * percentage)
       
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        summarizer = EdmundsonSummarizer()
        summarizer.bonus_words = get_stop_words("en")  # Words that will get a bonus in ranking
        summarizer.stigma_words = get_stop_words("en")  # Words that will get a penalty in ranking
        summarizer.null_words = get_stop_words("en")
        
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
                        
#     edmundson_summarization = Edmundson()
#     sentence_list, best_sentences, score_sentences = edmundson_summarization.summarize(text, 0, 0.5)   