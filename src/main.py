from src.model.SkipGram import SkipGram
from src.model.TFIDVect import TFIDVect


if __name__ == '__main__':
    skip_gram = SkipGram()
    skip_gram.train_skip_gram()

    # obj_TFIDVect = TFIDVect()
    # obj_TFIDVect.embed_method_name()
    # obj_TFIDVect.embed_method_comment()