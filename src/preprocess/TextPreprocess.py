import re

from bs4 import BeautifulSoup
from gensim.parsing import PorterStemmer
from nltk.corpus import stopwords

from src.config import AppConfig


class TextPreprocess:

    def __init__(self):
        self.ps = PorterStemmer()
        self.stopwords = stopwords.words("english")

    def remove_special_char(self, string_to_process):
        review = re.sub("[^a-zA-Z]", " ", string_to_process)
        return review

    def remove_tags(self, string_to_process):
        # parse html content
        soup = BeautifulSoup(string_to_process, "html.parser")

        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()
        # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)

    def remove_link_from(self, string_to_process):
        URLless_string = re.sub(
            r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}     /)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s('
            r')<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
            '', string_to_process)
        return URLless_string

        # Splitting sentence into words
        review = review.split()

    def stop_word_stemming(self, string_to_process):
        # Stemming
        # Stropwords removing
        string_to_process = string_to_process.split()
        review = [self.ps.stem(word) for word in string_to_process if word not in self.stopwords]

        # Joining the words again
        review = ' '.join(review)

        return review

    def process_method_name(self, api_name):

        # for prefix in AppConfig.LIBRARY_COMMON_PREFIX:
        #     if prefix in api_name:
        #         api_name = str(api_name).replace(prefix, "")
        #         break

        api_name_section = api_name.split(".")
        processed_api_name = ""

        for name_part in api_name_section:
            only_char = re.sub('\W+', '', name_part)
            camel_case = re.sub('(?<=[a-z])(?=[A-Z])', ' ', only_char).split(' ')
            single_string = ' '.join(camel_case)
            processed_api_name = processed_api_name + " " + single_string
            processed_api_name = processed_api_name.strip().lower()

        return processed_api_name

    def process_fully_qualified_api_name(self, fully_q_api_name):

        # fully_q_api_name = str(fully_q_api_name).replace(':', '.')

        api_name_section = fully_q_api_name.split(".")
        api_name_section = api_name_section[-2:]
        processed_api_name = ""

        for name_part in api_name_section:
            only_char = re.sub('\W+', '', name_part)
            camel_case = re.sub('(?<=[a-z])(?=[A-Z])', ' ', only_char).split(' ')
            single_string = ' '.join(camel_case)
            processed_api_name = processed_api_name + " " + single_string
            processed_api_name = processed_api_name.strip().lower()

        return processed_api_name

    def preprocess_test_api_name(self, api_name):
        api_name = re.sub(r'\([^)]*\)', '', api_name)
        api_name = api_name + '()'
        return api_name
