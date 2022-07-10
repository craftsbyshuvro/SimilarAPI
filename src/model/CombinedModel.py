from src.config import AppConfig
from src.model.SkipGram import SkipGram
from src.model.TFIDVect import TFIDVect
from src.preprocess.DataPreprocess import DataPreprocess
from src.temp.GraphEmbed import GraphEmbed


class CombinedModel:
    def __init__(self):
        self.obj_data_preprocess = DataPreprocess()
        self.obj_tfid_vect = TFIDVect()
        self.obj_skip_gram = SkipGram()
        self.graph_embedd = GraphEmbed()

    def get_combined_performance(self, graph_dict_data, graph_skip_gram_model, without_graph_skip_gram_model ,method_name_vectorizer, input_data):
        preprocessed_input_data = self.obj_data_preprocess.preprocess_input_data(input_data)

        # Using Graph
        # api_calling_sequence_similarity = self.graph_embedd.get_api_seq_similarity(preprocessed_input_data, graph_skip_gram_model, graph_dict_data)

        api_calling_sequence_similarity = self.obj_skip_gram.get_api_seq_similarity(preprocessed_input_data, without_graph_skip_gram_model)

        method_name_similarity = self.obj_tfid_vect.get_method_name_similarity(preprocessed_input_data, method_name_vectorizer)

        # method_comment = self.obj_tfid_vect.get_method_comment_similarity(preprocessed_input_data)

        # overall_similarity = api_calling_sequence_similarity * AppConfig.ALPHA + method_name_similarity * AppConfig.BETA + method_comment * AppConfig.GAMMA
        # Main one
        overall_similarity = api_calling_sequence_similarity * AppConfig.ALPHA + method_name_similarity * AppConfig.BETA


        return overall_similarity
