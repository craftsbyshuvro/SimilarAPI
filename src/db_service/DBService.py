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

    def get_all_method_name(self):
        method_comment_details_df = pd.read_sql_query("SELECT mcd.* FROM method_comment_details as mcd Where comment "
                                                      "is not null and comment_type = 'Javadoc' group by "
                                                      "mcd.file_path, mcd.method_name", self.con)
        return method_comment_details_df

    def get_all_method_comment(self):
        method_comment_details_df = pd.read_sql_query("SELECT mcd.* FROM method_comment_details as mcd Where comment "
                                                      "is not null and comment_type = 'Javadoc' group by "
                                                      "mcd.file_path, mcd.comment", self.con)
        return method_comment_details_df

    def get_all_import_statement(self):
        import_statement_df = pd.read_sql_query("SELECT * from import_statement", self.con)
        return import_statement_df

    def get_api_names_with_prior_comment(self):
        api_names = pd.read_sql_query("SELECT ac.id, ac.file_path, ac.declared_method, ac.invoked_method FROM "
                                      "api_call_sequence AS ac JOIN ( SELECT metho_c_d.file_path, "
                                      "metho_c_d.method_name FROM method_comment_details AS metho_c_d WHERE "
                                      "metho_c_d.comment_type = 'Javadoc' GROUP BY metho_c_d.file_path, "
                                      "metho_c_d.method_name ) AS mcd ON ac.file_path = mcd.file_path AND "
                                      "ac.declared_method = mcd.method_name", self.con)
        return api_names
