# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:41:37 2024

@author: LCC Abraham Saul Sandoval Meneses

OpenAI API - Chat GTP Summarization.

"""

import nltk
import os
from openai import OpenAI

class GPT():
    
    def __init__(self):
        super().__init__()
        
    def summarize(self, text):
        
        client = OpenAI(
          api_key=os.environ['OPENAI_API_KEY']  
        )
        
        original_sentences = [sentence for sentence in nltk.sent_tokenize(text)]
        
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {
              "role": "system",
              "content": "Perform a text summarization and shorten the text as the half"
            },
            {
              "role": "user",
              "content": text
            }
          ],
          temperature=0.5,
          top_p=1
        )
        
        summary = response.choices[0].message.content;
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
                        
#     gpt_summarization = GPTSummarizer()
#     sentence_list, best_sentences, score_sentences = gpt_summarization.summarize(text)   