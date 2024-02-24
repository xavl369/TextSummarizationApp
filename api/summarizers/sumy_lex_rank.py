# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:28:42 2024

@author: LCC Abraham Saul Sandoval Meneses

Sumy - LexRank

Unsupervised approach inspired by algorithms PageRank and HITS - algorithms inspired on the world wide web. 
They try to find connections between the sentences and identify the ones connected with the most significant words/topics. 
You should read the original papers to find out if they are suitable for your use-case.
"""

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from summarizers.text_summarization_base import TextSummarizer
    
class LexRank(TextSummarizer):
    
    def __init__(self):
        super().__init__()
        
    def summarize(self, text, number_of_sentences, percentage = 0):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        if percentage > 0:
            number_of_sentences = int(len(original_sentences) * percentage)
        
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
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
                        
#     lex_rank_summarization = LexRank()
#     sentence_list, best_sentences, score_sentences = lex_rank_summarization.summarize(text, 0, 0.5)   