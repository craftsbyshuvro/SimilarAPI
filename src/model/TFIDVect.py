from scipy import spatial
from tabulate import tabulate
import pandas as pd
from src.preprocess.DataPreprocess import DataPreprocess
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class TFIDVect:
    def __init__(self):
        self.pre_process_service = DataPreprocess()

    def check_cosine_similarity(self):
        pass

    def embed_method_name(self):
        method_name = self.pre_process_service.get_preprocessed_method_name()
        method_names = list(method_name['method_name'])

        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform(method_names)

        source_api = vectorizer.transform(['game manager'])
        target_api = vectorizer.transform(['game ended'])
        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)
        print("Method Name Cosine Similarity: ", cosine_similarity)

    def embed_method_comment(self):
        method_comment = self.pre_process_service.get_preprocessed_method_comment()
        method_comments = list(method_comment['comment'])

        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform(method_comments)

        source_api = vectorizer.transform(['param enabl'])
        target_api = vectorizer.transform(['param view'])
        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)
        print("Method Comment Cosine Similarity: ", cosine_similarity)
