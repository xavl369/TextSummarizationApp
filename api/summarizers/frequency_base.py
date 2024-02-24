# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:12:21 2024

@author: LCC Abraham Saul Sandoval Meneses

Natural Language Processing for Text Summarization

Automatic Summarization: Frequency Based Algorithm

Text summarization

Steps
1.- Preprocessing the texts
2.- Word Frequency
3.- Weighted word frequency
4.- Sentence tokenization
5.- Score for the sentences
6.- Order the sentences
7.- Generate Summary

Important Points:
1.- Define the size or length of the summary, and will be based on the size of the original text
the bigger the text, the bigger the summary must be

Its necessary because if you have a long text and you choose only a few sentences, this summary 
will not be so good because not all important sentences will be returned


2.- The evaluation of the summary is somewhat abstract so we need to read only the main sentences 
and check if the general idea of the text can be understand

There are some ways to evaluate this type of algorthms, like share the text to other peoples to read,
meake a questionarie and with the original text and try to answer the questions with the text summarization

"""

import nltk
import heapq 
from summarizers.text_summarization_base import TextSummarizer

class FrequencyBased(TextSummarizer):
    
    def __init__(self):
        super().__init__()
    
    def calculate_score_sentence(self, sentence_list, word_frequency):
        
        score_sentences = {}
        
        for sentence in sentence_list:
          for word in nltk.word_tokenize(sentence):
            if word in word_frequency.keys():
              if sentence not in score_sentences.keys():
                score_sentences[sentence] = word_frequency[word]
              else:
                score_sentences[sentence] += word_frequency[word]
                
        return score_sentences
    
    
    def words_frequency(self, formatted_text):
        word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))
        highest_frequency = max(word_frequency.values())
        for word in word_frequency.keys():
          word_frequency[word] = (word_frequency[word] / highest_frequency)
      
        return word_frequency
        
        
    def summarize(self, text, number_of_sentences, percentage = 0):
     
        formatted_text = self.preprocess(text)
        
        word_frequency = self.words_frequency(formatted_text)
        sentence_list = nltk.sent_tokenize(text)

        score_sentences = self.calculate_score_sentence(sentence_list, word_frequency)
       
        if percentage > 0:
          best_sentences = heapq.nlargest(int(len(sentence_list) * percentage), score_sentences, key=score_sentences.get)
        else:
          best_sentences = heapq.nlargest(number_of_sentences, score_sentences, key=score_sentences.get)
          
        return sentence_list, best_sentences, score_sentences
    

# if __name__ == "__main__":
#     text = """Artificial intelligence is human like intelligence. 
#                         It is the study of intelligent artificial agents. 
#                         Science and engineering to produce intelligent machines. 
#                         Solve problems and have intelligence. 
#                         Related to intelligent behavior. 
#                         Developing of reasoning machines. 
#                         Learn from mistakes and successes. 
#                         Artificial intelligence is related to reasoning in everyday situations."""
                        
#     frequency_based_summarization = FrequencyBased()
#     sentence_list, best_sentences, score_sentences = frequency_based_summarization.summarize(text, 0, 0.5)    
    
                       