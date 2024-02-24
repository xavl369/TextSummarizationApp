# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:45:02 2024

@author: LCC Abraham Saul Sandoval Meneses


Bert Extractive Summarizer

This tool utilizes the HuggingFace Pytorch transformers library to run extractive summarizations. 
This works by first embedding the sentences, then running a clustering algorithm, finding the sentences that are closest to the cluster's centroids.


https://pypi.org/project/bert-extractive-summarizer/
"""

import nltk
from summarizer import Summarizer


class Bert():
    
    def __init__(self):
        super().__init__()
        
    def summarize(self, text):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        summarizer = Summarizer()
        summary = summarizer(text)
        best_sentences = [sentence for sentence in nltk.sent_tokenize(summary)]
        
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
                        
#     bert_summarization = BertSummarizer()
#     sentence_list, best_sentences, score_sentences = bert_summarization.summarize(text)   