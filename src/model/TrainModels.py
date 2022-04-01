from src.model.SkipGram import SkipGram
from src.model.TFIDVect import TFIDVect

class TrainModel:
    def __init__(self):
        self.obj_skip_gram = SkipGram()
        self.obj_tfid = TFIDVect()

    def train_skip_gram(self):
        self.obj_skip_gram.train_skip_gram()

    def embed_method_name(self):
        self.obj_tfid.embed_method_name()

    def embed_method_comment(self):
        self.obj_tfid.embed_method_comment()
