# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:06:37 2024

@author: LCC Abraham Saul Sandoval Meneses


Sumy - LSA: Latent Semantic Analysis
Algebraic method - the most advanced method is independent of the language. 
But also the most complicated (computationally and mentally).
The method is able to identify synonyms in the text and the topics that are not explicitly written in the Document. 
The best for the plain text documents without any markup but it shines also for the HTML documents. 
I think the author is using more advanced algorithms now described in Steinberger, J. a Ježek, K. Using latent semantic an and summary evaluation.
In In Proceedings ISIM ‘04. 2004. S. 93-100..
"""


import nltk
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from summarizers.text_summarization_base import TextSummarizer

class Lsa(TextSummarizer):
    
    def __init__(self):
        super().__init__()
        
    def summarize(self, text, number_of_sentences, percentage = 0):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        if percentage > 0:
            number_of_sentences = int(len(original_sentences) * percentage)
        
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
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
                        
#     lsa_summarization = Lsa()
#     sentence_list, best_sentences, score_sentences = lsa_summarization.summarize(text, 0, 0.5)   