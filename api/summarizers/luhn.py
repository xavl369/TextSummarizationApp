# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:50:31 2024

@author: abrah


Lunn Algorithm

Developed by Hans Peter Luhn in 1958, is a classic and influential approach to text summarization. 
While considered a "naive" method compared to more modern techniques, it remains a valuable tool for its simplicity and interpretability. 

Steps:
    
1.- Create list of sentences   
2.- Preprocess sentences
3.- Count how many times each word appear in each sentence
4.- Take most important (frequent) words
5.- Ccalculate scores
6.- order best sentences
7.- Get the best sentences text


Important Points:
    
1. Select most important words based frequency
2. Score calculation: The most important sentence
3. The more words in the same group, the more important this sentence is
4. Groups are used to calculate the score of the sentences

"""


import nltk
import heapq 
from summarizers.text_summarization_base import TextSummarizer

class Luhn(TextSummarizer):
    
    def __init__(self):
        super().__init__()

    def calculate_score_sentence(self, sentences, important_words, distance):
    
      scores = [] #score for each sentence
      sentence_index = 0 #index for each sentence
    
      #get each sentence to get each word regarding the sentence
      for sentence in [nltk.word_tokenize(sentence) for sentence in sentences]:
       
        #get the sentence index for the word that is contained in the important words
        word_index = []
        for word in important_words:
    
          try:
            word_index.append(sentence.index(word))
          except ValueError:
            pass
    
        word_index.sort()
       
        #if the sentence does not present am important word
        if len(word_index) == 0:
          continue
    
        groups_list = []
        group = [word_index[0]]
        i = 1 # 3
        
        #group the words according to distance parameter
        while i < len(word_index): # 3
          # first execution: 1 - 0 = 1
          # second execution: 2 - 1 = 1
          if word_index[i] - word_index[i - 1] < distance:
            group.append(word_index[i])
           
          else:
            groups_list.append(group[:]) #[:] access all elements on the list
            group = [word_index[i]]
           
          i += 1
          
        groups_list.append(group)
       
        #calculate score for each group
        max_group_score = 0
        for g in groups_list:
         
          important_words_in_group = len(g)
          total_words_in_group = g[-1] - g[0] + 1
          score = 1.0 * important_words_in_group**2 / total_words_in_group
         
          #best score
          if score > max_group_score:
            max_group_score = score
            
        #score foe each sentence
        scores.append((max_group_score, sentence_index))
        sentence_index += 1
    
      #print('final scores', scores)
      return scores
        
    
    def summarize(self, text, number_of_sentences = 0, percentage = 0.5, top_n_words = 150, distance=1):
      #1. create list of sentences   
      original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
      
      #2. preprocessing sentences
      formatted_sentences = [self.preprocess(original_sentence) for original_sentence in original_sentences]
      
      #3. count how many times each word appear in each sentence
      words = [word for sentence in formatted_sentences for word in nltk.word_tokenize(sentence)]
      frequency = nltk.FreqDist(words)
      
      #4. take most important (frequent) words
      top_n_words = [word[0] for word in frequency.most_common(top_n_words)]
      
      #5. calculate scores
      sentences_score = self.calculate_score_sentence(formatted_sentences, top_n_words, distance)
    
      #6 order best sentences
      if percentage > 0:
        best_sentences = heapq.nlargest(int(len(formatted_sentences) * percentage), sentences_score)
      else:  
        best_sentences = heapq.nlargest(number_of_sentences, sentences_score)
      
      #7 get the best sentences text
      best_sentences = [original_sentences[i] for (score, i) in best_sentences]
      
      return original_sentences, best_sentences, sentences_score
  
    
  
    
# if __name__ == "__main__":
#     text = """Artificial intelligence is human like intelligence. 
#                         It is the study of intelligent artificial agents. 
#                         Science and engineering to produce intelligent machines. 
#                         Solve problems and have intelligence. 
#                         Related to intelligent behavior. 
#                         Developing of reasoning machines. 
#                         Learn from mistakes and successes. 
#                         Artificial intelligence is related to reasoning in everyday situations."""
                        
#     luhn_summarization = Luhn()
#     sentence_list, best_sentences, score_sentences = luhn_summarization.summarize(text, 0, 0.5)    
    