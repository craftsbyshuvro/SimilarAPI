from scipy import spatial
from tabulate import tabulate

from src.preprocess.DataPreprocess import DataPreprocess
from gensim.models import Word2Vec


class SkipGram:
    def __init__(self):
        self.pre_process_service = DataPreprocess()

    def train_skip_gram(self):
        api_call_sequence = self.pre_process_service.preprocess_api_call_sequence()

        invoked_methods_sentences = list(api_call_sequence['invoked_method'])

        word_tokenizer = []

        for sent in invoked_methods_sentences:
            word_tokens = sent.split()
            word_tokenizer.append(word_tokens)

        model_skip_gram = Word2Vec(sentences=word_tokenizer, window=5, sg=1)

        source_api_vector = model_skip_gram.wv['java.lang.String.equalsIgnoreCase']
        target_api_vector = model_skip_gram.wv['org.bigbluebutton.core.api.IBigBlueButtonInGW.handleJsonMessage']

        cosine_similarity = 1 - spatial.distance.cosine(source_api_vector, target_api_vector)
        print(cosine_similarity)