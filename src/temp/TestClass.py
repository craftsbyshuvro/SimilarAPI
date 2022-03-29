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

        vectorizer = CountVectorizer()

        X = vectorizer.fit_transform(corpus)
        print(vectorizer.get_feature_names())
        print(X.toarray())

        print(vectorizer.transform(['not in any of the document second second']).toarray())
