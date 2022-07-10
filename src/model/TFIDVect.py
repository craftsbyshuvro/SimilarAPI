import joblib
from scipy import spatial
from sklearn.feature_extraction.text import TfidfVectorizer
from tabulate import tabulate

from src.config import AppConfig
from src.preprocess.DataPreprocess import DataPreprocess


class TFIDVect:
    def __init__(self):
        self.pre_process_service = DataPreprocess()

    def embed_method_name(self):
        method_name = self.pre_process_service.get_preprocessed_method_name()
        method_names = list(method_name['method_name'])

        vectorizer = TfidfVectorizer()
        vectorizer.fit_transform(method_names)

        joblib.dump(vectorizer, AppConfig.TFID_MODEL_PATH_METHOD_NAME)

        print('TFID Method Name vector trained and saved successfully')

    def get_method_name_similarity(self, input_data, model_vect):

        if model_vect is None:
            method_name_vectorizer = joblib.load(AppConfig.TFID_MODEL_PATH_METHOD_NAME)
        else:
            method_name_vectorizer = model_vect


        source_method_name = input_data['source_api_name_fully_qualified_processed']
        target_method_name = input_data['target_api_name_fully_qualified_processed']

        source_api = method_name_vectorizer.transform([source_method_name])
        target_api = method_name_vectorizer.transform([target_method_name])

        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)

        return cosine_similarity

    def embed_method_comment(self):
        method_comment = self.pre_process_service.get_preprocessed_method_comment()
        method_comments = list(method_comment['comment'])

        vectorizer = TfidfVectorizer()
        vectorizer.fit_transform(method_comments)

        joblib.dump(vectorizer, AppConfig.TFID_MODEL_PATH_METHOD_COMMENT)

        print('TFID Method Comment vector trained and saved successfully', end="\n\n")

    def get_method_comment_similarity(self, input_data, model_vect = None):

        if model_vect is None:
            method_comment_vectorizer = joblib.load(AppConfig.TFID_MODEL_PATH_METHOD_COMMENT)
        else:
            method_comment_vectorizer = model_vect

        source_method_comment = input_data['source_api_description_processed']
        target_method_comment = input_data['target_api_description_processed']

        source_api = method_comment_vectorizer.transform([source_method_comment])
        target_api = method_comment_vectorizer.transform([target_method_comment])

        source_api = source_api.toarray()[0]
        target_api = target_api.toarray()[0]

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)

        return cosine_similarity

    def embed_method_api_name(self):
        method_name = self.pre_process_service.get_preprocesed_api_names()
        invoked_methods = list(method_name['invoked_method'])

        vectorizer = TfidfVectorizer()
        vectorizer.fit_transform(invoked_methods)

        joblib.dump(vectorizer, AppConfig.TFID_MODEL_PATH_METHOD_NAME)

        print('TFID Method Name vector trained and saved successfully')
