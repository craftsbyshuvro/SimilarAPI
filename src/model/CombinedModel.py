from src.config import AppConfig
from src.model.SkipGram import SkipGram
from src.model.TFIDVect import TFIDVect
from src.preprocess.DataPreprocess import DataPreprocess


class CombinedModel:
    def __init__(self):
        self.obj_data_preprocess = DataPreprocess()
        self.obj_tfid_vect = TFIDVect()
        self.obj_skip_gram = SkipGram()

    def get_combined_performance(self, input_data):
        preprocessed_input_data = self.obj_data_preprocess.preprocess_input_data(input_data)

        api_calling_sequence_similarity = self.obj_skip_gram.train_skip_gram(preprocessed_input_data)
        method_name_similarity = self.obj_tfid_vect.embed_method_name(preprocessed_input_data)
        method_comment = self.obj_tfid_vect.embed_method_comment(preprocessed_input_data)

        overall_similarity = api_calling_sequence_similarity * AppConfig.ALPHA + method_name_similarity * AppConfig.BETA + method_comment * AppConfig.GAMMA

        return overall_similarity
