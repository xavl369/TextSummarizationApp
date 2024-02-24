# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:44:36 2023

@author: LCC Abraham Saul Sandoval Meneses

Text Summarization API 
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from text_summarization_factory import TextSummarizerFactory
import os

app = Flask(__name__)
CORS(app)


@app.before_request
def before_request():
    if request.method != 'OPTIONS':
        api_key = request.headers.get('Authorization')
        if not api_key or api_key != os.environ['SUMMARIZATION_API_KEY']:
            return jsonify({'error': 'Unauthorized'}), 401


@app.route('/api/text-summarization', methods=['POST'])
def summarize():

    try:
        
        # Perform text summarization
        data = request.get_json()
        summarizer = TextSummarizerFactory(data['method'])
        params = TextSummarizerFactory.create_params(data['text'], 0, 0.5, 150, 1)
        original_sentence, best_sentences, score_sentences = summarizer.summarize(params)
    
        # Return the summarized data
        return jsonify({"sentence_list":  original_sentence, 
                        "best_sentences": best_sentences,
                        "score_sentences": score_sentences,
                        "method": data['method']
                        }), 200
    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({"error" : str(e)}), 500
        
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)