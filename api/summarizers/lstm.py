# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:39:14 2024

@author: LCC Abraham Saul Sandoval Meneses

Automatic Summarization Library: pysummarization

The function of this library is automatic summarization using a kind of natural language processing and neural network language model. 
This library enable you to create a summary with the major points of the original document or web-scraped text that filtered by text clustering. 
And this library applies accel-brain-base to implement Encoder/Decoder based on LSTM improving the accuracy of summarization by Sequence-to-Sequence(Seq2Seq) learning.


https://pypi.org/project/pysummarization/
"""


import nltk
import re
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from summarizers.text_summarization_base import TextSummarizer


class LSTM(TextSummarizer):
    
    def __init__(self):
        super().__init__()
        
    def summarize(self, text):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        auto_abstractor = AutoAbstractor()
        auto_abstractor.tokenizable_doc = SimpleTokenizer()
        auto_abstractor.delimiter_list = ['.', '\n']
        abstractable_doc = TopNRankAbstractor()
        
        summary = auto_abstractor.summarize(text, abstractable_doc)
        print(summary['summarize_result'])
   
        best_sentences = []
        for sentence in summary['summarize_result']:
            if sentence != '|n':
                best_sentences.append(re.sub(r'\s+', ' ', sentence).strip())
        
        best_sentences = list(filter(lambda x: x != "", best_sentences))
        return original_sentences, best_sentences, summary['scoring_data']



# if __name__ == "__main__":
#     text = """Artificial intelligence is human like intelligence. 
#                         It is the study of intelligent artificial agents. 
#                         Science and engineering to produce intelligent machines. 
#                         Solve problems and have intelligence. 
#                         Related to intelligent behavior. 
#                         Developing of reasoning machines. 
#                         Learn from mistakes and successes. 
#                         Artificial intelligence is related to reasoning in everyday situations."""
                        
#     lstm_summarization = LSTMSummarization()
#     sentence_list, best_sentences, score_sentences = lstm_summarization.summarize(text)   