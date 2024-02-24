# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:08:19 2024

@author: LCC Abraham Saul Sandoval Meneses

Cosine similarity

Important Points:

1.- Mathematical calculations are made in order to get similarity between sentences
2.- Convert sentences from string to vectors in order to be able to calculate this similarity between them
3.- Higher the value, the greater the similarity between sentences
4.- The more words in common, the greater the similarity

"""

import networkx as nx
import nltk
import numpy as np

from nltk.cluster.util import cosine_distance
from summarizers.text_summarization_base import TextSummarizer

class CosineSimilarity(TextSummarizer):
    
    def __init__(self):
        super().__init__()
        
    #calculate similarity between sentences
    def calculate_sentence_similarity(self, sentence1, sentence2):
        
      words1 = [word for word in nltk.word_tokenize(sentence1)]
      words2 = [word for word in nltk.word_tokenize(sentence2)]
    
      all_words = list(set(words1 + words2)) #unique words
    
      vector1 = [0] * len(all_words)
      vector2 = [0] * len(all_words)
     
      for word in words1: # Bag of words
        vector1[all_words.index(word)] += 1
        
      for word in words2:
        vector2[all_words.index(word)] += 1
      
      return 1 - cosine_distance(vector1, vector2)
  
    
    # The higher the value, the greater the similarity between the sentences
    # The more words in common, the greater the similarity
    def calculate_similarity_matrix(self, sentences):
        
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
        for i in range(len(sentences)):
            for j in range(len(sentences)):
                
                if i == j:
                    continue
                else:
                    similarity_matrix[i][j] = self.calculate_sentence_similarity(sentences[i], sentences[j])
                
        return similarity_matrix
        
        
    def summarize(self, text, number_of_sentences, percentage = 0):
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        formatted_sentences = [self.preprocess(original_sentence) for original_sentence in original_sentences]
        
        #relation between sentences
        similarity_matrix = self.calculate_similarity_matrix(formatted_sentences)
        similarity_graph = nx.from_numpy_array(similarity_matrix)
        
        #measure importante of each one of the sentences based on their relations
        scores = nx.pagerank(similarity_graph) 
        ordered_scores = sorted(((scores[i], score) for i, score in enumerate(original_sentences)), reverse=True) #higher values
       
      
        if percentage > 0:
          number_of_sentences = int(len(formatted_sentences) * percentage)
      
        best_sentences = [ordered_scores[sentence][1] for sentence in range(number_of_sentences)] #(position 0: score, position 1: sentence)
        
        return original_sentences, best_sentences, ordered_scores
    
    
    
# if __name__ == "__main__":
#     text = """Artificial intelligence is human like intelligence. 
#                         It is the study of intelligent artificial agents. 
#                         Science and engineering to produce intelligent machines. 
#                         Solve problems and have intelligence. 
#                         Related to intelligent behavior. 
#                         Developing of reasoning machines. 
#                         Learn from mistakes and successes. 
#                         Artificial intelligence is related to reasoning in everyday situations."""
                        
#     cocine_similarity_summarization = CosineSimilarity()
#     sentence_list, best_sentences, score_sentences = cocine_similarity_summarization.summarize(text, 0, 0.5)   
    