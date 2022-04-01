from tabulate import tabulate
import pandas as pd
import re

from src.config import AppConfig
from src.db_service.DBService import DBService
from src.preprocess.TextPreprocess import TextPreprocess


class DataPreprocess:
    def __init__(self):
        self.db_service = DBService()
        ignore_list = ['TODO:', 'Created by IntelliJ IDEA', 'Created with IntelliJ IDEA', 'User:',
                       'Data:', 'Name:']
        self.ignore_comment_starts_with = [x.lower() for x in ignore_list]
        self.obj_text_preprocess = TextPreprocess()

    def preprocess_api_call_sequence(self):
        api_call_sequence = self.db_service.get_all_api_call_sequences()

        api_call_sequence = api_call_sequence

        pre_processed_data = list()
        for index, row in api_call_sequence.iterrows():
            invoked_method = str(row['invoked_method']).strip()
            if "UNKNOWN" in invoked_method or invoked_method is None or invoked_method == '':
                continue

            # invoked_method = invoked_method.replace("()", "").replace(":", ".")

            pre_processed_data.append({'file_path': row['file_path'],
                                       'declared_method': row['declared_method'],
                                       'invoked_method': invoked_method})

        pre_processed_df = pd.DataFrame(pre_processed_data)

        pre_processed_df = pre_processed_df.groupby(['file_path', 'declared_method'], as_index=False).agg(
            {'invoked_method': ' '.join})
        return pre_processed_df

    def get_first_line_after_preprocess(self, comment_list):
        for comment in comment_list:
            processed_com = str(comment).strip().lower()
            if len(processed_com) > 0:
                if processed_com.startswith(tuple(self.ignore_comment_starts_with)):
                    return None
                else:
                    processed_text = self.obj_text_preprocess.remove_tags(processed_com)
                    processed_text = self.obj_text_preprocess.remove_link_from(processed_text)
                    processed_text = self.obj_text_preprocess.stop_word_stemming(processed_text)
                    processed_text = self.obj_text_preprocess.remove_special_char(processed_text)
                    processed_text = processed_text.strip()
                    return processed_text

    def preprocess_method_comment(self):
        method_comment_detail = self.db_service.get_all_method_comment_detail()

        pre_processed_data = list()
        for index, row in method_comment_detail.iterrows():
            method_comment = str(row['comment']).strip()
            method_name = str(row['method_name']).strip()

            method_comment = re.sub(r'[^ \nA-Za-z0-9]+', '', method_comment)
            method_comment = method_comment.splitlines()

            comment = self.get_first_line_after_preprocess(method_comment)

            if comment is None:
                continue

            method_name = self.obj_text_preprocess.process_method_name(method_name)

            pre_processed_data.append({'file_path': row['file_path'],
                                       'method_name': method_name,
                                       'comment': comment})

        pre_processed_df = pd.DataFrame(pre_processed_data)
        pre_processed_df = pre_processed_df.groupby('file_path').agg(lambda x: ' '.join(x))

        # pre_processed_df["method_name"] = pre_processed_df["method_name"].apply(lambda x: x.replace(".", ""))
        # pre_processed_df["comment"] = pre_processed_df["comment"].apply(lambda x: x.replace(".", ""))

        return pre_processed_df

    def get_preprocessed_method_name(self):
        pre_processed_df = self.preprocess_method_comment()
        method_name = pd.DataFrame(pre_processed_df['method_name'])
        return method_name

    def get_preprocessed_method_comment(self):
        pre_processed_df = self.preprocess_method_comment()
        comment = pd.DataFrame(pre_processed_df['comment'])
        return comment

    def preprocess_input_data(self, input_data):
        source_api_name_fully_qualified = input_data['source_api_name_fully_qualified']
        source_api_description = input_data['source_api_description']

        source_api_name_fully_qualified_processed = self.obj_text_preprocess.process_fully_qualified_api_name(
            source_api_name_fully_qualified)
        source_api_description_processed = self.get_first_line_after_preprocess([source_api_description])

        target_api_name_fully_qualified = input_data['target_api_name_fully_qualified']
        target_api_description = input_data['target_api_description']

        target_api_name_fully_qualified_processed = self.obj_text_preprocess.process_fully_qualified_api_name(
            target_api_name_fully_qualified)
        target_api_description_processed = self.get_first_line_after_preprocess([target_api_description])

        processed_input_data = {'source_api_name_fully_qualified_processed': source_api_name_fully_qualified_processed,
                                'source_api_description_processed': source_api_description_processed,
                                'target_api_name_fully_qualified_processed': target_api_name_fully_qualified_processed,
                                'target_api_description_processed': target_api_description_processed,
                                'source_api_name_fully_qualified_raw': source_api_name_fully_qualified,
                                'target_api_name_fully_qualified_raw': target_api_name_fully_qualified
                                }

        return processed_input_data

    def get_preprocesed_api_names(self):
        api_names_prior_comment = self.db_service.get_api_names_with_prior_comment()
        pre_processed_data = list()
        for index, row in api_names_prior_comment.iterrows():
            invoked_method = str(row['invoked_method']).strip()

            invoked_method = self.obj_text_preprocess.process_fully_qualified_api_name(invoked_method)

            pre_processed_data.append({'file_path': row['file_path'],
                                       'invoked_method': invoked_method})

        pre_processed_df = pd.DataFrame(pre_processed_data)
        pre_processed_df = pre_processed_df.groupby('file_path').agg(lambda x: ' '.join(x))

        return pre_processed_df
