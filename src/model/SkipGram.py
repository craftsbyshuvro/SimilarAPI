from scipy import spatial
from tabulate import tabulate

from src.preprocess.DataPreprocess import DataPreprocess
from gensim.models import Word2Vec
import numpy as np


class SkipGram:
    def __init__(self):
        self.pre_process_service = DataPreprocess()
        self.embeddingsSize = 500
        self.model_skip_gram = None

    def train_skip_gram(self, input_data):
        source_api = input_data['source_api_name_fully_qualified_raw']
        target_api = input_data['target_api_name_fully_qualified_raw']

        api_call_sequence = self.pre_process_service.preprocess_api_call_sequence()
        invoked_methods_sentences = list(api_call_sequence['invoked_method'])

        word_tokenizer = []

        for sent in invoked_methods_sentences:
            word_tokens = sent.split()
            word_tokenizer.append(word_tokens)

        self.model_skip_gram = Word2Vec(sentences=word_tokenizer, window=5, sg=1, min_count=1, workers=4,
                                        vector_size=self.embeddingsSize)

        source_api_vector = self.model_skip_gram.wv[source_api]
        target_api_vector = self.model_skip_gram.wv[target_api]

        cosine_similarity = 1 - spatial.distance.cosine(source_api_vector, target_api_vector)

        return cosine_similarity