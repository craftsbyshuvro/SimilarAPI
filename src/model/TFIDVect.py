from scipy import spatial
from tabulate import tabulate
import pandas as pd
from src.preprocess.DataPreprocess import DataPreprocess
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class TFIDVect:
    def __init__(self):
        self.pre_process_service = DataPreprocess()

    def embed_method_name(self, input_data):
        source_method_name = input_data['source_api_name_fully_qualified_processed']
        target_method_name = input_data['target_api_name_fully_qualified_processed']

        method_name = self.pre_process_service.get_preprocessed_method_name()
        method_names = list(method_name['method_name'])

        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform(method_names)

        source_api = vectorizer.transform([source_method_name])
        target_api = vectorizer.transform([target_method_name])

        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)

        return cosine_similarity

    def embed_method_comment(self, input_data):
        source_method_comment = input_data['source_api_description_processed']
        target_method_comment = input_data['target_api_description_processed']

        method_comment = self.pre_process_service.get_preprocessed_method_comment()
        method_comments = list(method_comment['comment'])

        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform(method_comments)

        source_api = vectorizer.transform([source_method_comment])
        target_api = vectorizer.transform([target_method_comment])
        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)

        return cosine_similarity
