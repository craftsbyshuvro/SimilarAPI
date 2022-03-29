import sqlite3

from src.config import AppConfig
import pandas as pd


class DBService:
    def __init__(self):
        self.con = sqlite3.connect(AppConfig.DB_CON_STRING)

    def get_data_by_query(self, sql_query):
        df = pd.read_sql_query(sql_query, self.con)
        return df

    def get_all_api_call_sequences(self):
        api_call_sequence_df = pd.read_sql_query("SELECT file_path, declared_method, invoked_method from "
                                                 "api_call_sequence", self.con)
        return api_call_sequence_df

    def get_all_method_comment_detail(self):
        method_comment_details_df = pd.read_sql_query("SELECT * from method_comment_details where comment is not null "
                                                      "and comment_type = 'Javadoc'", self.con)
        return method_comment_details_df

    def get_all_import_statement(self):
        import_statement_df = pd.read_sql_query("SELECT * from import_statement", self.con)
        return import_statement_df
