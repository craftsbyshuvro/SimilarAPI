from scipy import spatial
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class TestClass:
    def test_method(self):
        corpus = [
            'This is the first document.',
            'This document is the second document.',
            'And this is the third one.',
            'Is this the first document?']

        vectorizer = TfidfVectorizer()

        # embed corpus in vector space
        X = vectorizer.fit_transform(corpus)

        # Getting vector for source and target api using embedded corpus
        source_api = vectorizer.transform(['not in any of the document second']).toarray()
        target_api = vectorizer.transform(['not in any of the document second second']).toarray()

        cosine_similarity = 1 - spatial.distance.cosine(source_api, target_api)

        print(cosine_similarity)
