import itertools
from operator import itemgetter

from tqdm import tqdm

from src.config import AppConfig
from src.helper.Helper import Helper
from src.model.CombinedModel import CombinedModel
from src.model.TrainModels import TrainModel
import pandas as pd
import re

from src.preprocess.DataPreprocess import DataPreprocess
from src.preprocess.TextPreprocess import TextPreprocess
from src.temp.GraphEmbed import GraphEmbed

if __name__ == '__main__':
    objge = GraphEmbed()
    objge.embed()




    # ====================TRAIN=========================

    # obj_train_model = TrainModel()
    #
    # obj_train_model.train_skip_gram()
    # # obj_train_model.embed_method_name()
    #
    # # This is what i understand
    # obj_train_model.embed_method_api_name()
    #
    # obj_train_model.embed_method_comment()

    # ====================TEST=========================

    # obj_text_preprocess = TextPreprocess()
    # obj_data_preprocess = DataPreprocess()
    # obj_combined_performance = CombinedModel()
    #
    # source_data = pd.read_csv(AppConfig.COMMON_IO_TEST_DATA)
    # target_data = pd.read_csv(AppConfig.GOOGLE_IO_TEST_DATA)
    #
    # ground_truth = obj_data_preprocess.process_ground_truth(AppConfig.IO_GROUND_TRUTH)
    # all_test_results = []
    # comparison_with_ground_result = []
    #
    # for index_s, test_s in source_data.iterrows():
    #     test_results = []
    #     source_api_track = ''
    #     target_api_track = ''
    #     comparison_with_ground_truth = {}
    #     for index_t, test_t in target_data.iterrows():
    #         print("Processing No: ", index_s + 1, ' | with: ', index_t + 1)
    #
    #         test_s['api_name'] = obj_text_preprocess.preprocess_test_api_name(
    #             test_s['api_name'])
    #         test_t['api_name'] = obj_text_preprocess.preprocess_test_api_name(
    #             test_t['api_name'])
    #
    #         input_data = {'source_api_name_fully_qualified': test_s['api_name'],
    #                       'source_api_description': test_s['api_description'],
    #                       'target_api_name_fully_qualified': test_t['api_name'],
    #                       'target_api_description': test_t['api_description']
    #                       }
    #         try:
    #             overall_similarity = obj_combined_performance.get_combined_performance(input_data)
    #         except:
    #             overall_similarity = 0
    #
    #         print("Score:   ", overall_similarity)
    #         test_result = dict()
    #         test_result['source_api'] = test_s['api_name']
    #         test_result['target_api'] = test_t['api_name']
    #         test_result['similarity_score'] = overall_similarity
    #
    #         test_result['source_api'] = str(test_result['source_api']).split('(', 1)[0]
    #         test_result['target_api'] = str(test_t['api_name']).split('(', 1)[0]
    #         source_api_track = test_result['source_api']
    #         target_api_track = test_result['target_api']
    #         test_results.append(test_result)
    #
    #     sorted_result = sorted(test_results, key=itemgetter('similarity_score'), reverse=True)
    #
    #     ground_truth_for_source_api = [d['target_api'] for d in ground_truth if d['source_api'] in [source_api_track]]
    #     sorted_result = pd.DataFrame(sorted_result).groupby(['source_api', 'target_api'], as_index=False).first()
    #
    #     sorted_result_sorted = sorted_result.to_dict(orient='records')
    #     sorted_result_sorted = sorted(sorted_result_sorted, key=itemgetter('similarity_score'), reverse=True)
    #
    #     truth_indices = [i for i, x in enumerate(sorted_result_sorted) if
    #                      x['target_api'] in ground_truth_for_source_api]
    #
    #     comparison_with_ground_truth['source_api'] = source_api_track
    #     comparison_with_ground_truth['target_api'] = target_api_track
    #     if len(truth_indices) == 0:
    #         truth_rank = -1
    #     else:
    #         truth_rank = min(truth_indices) + 1
    #
    #     comparison_with_ground_truth['truth_rank'] = truth_rank
    #     comparison_with_ground_result.append(comparison_with_ground_truth)
    #
    #     all_test_results = all_test_results + sorted_result_sorted
    #
    # all_test_results_df = pd.DataFrame(all_test_results)
    # all_test_results_df.to_csv("D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\similarity_score.csv",
    #                            index=False)
    #
    # comparison_with_ground_result = pd.DataFrame(comparison_with_ground_result)
    # comparison_with_ground_result.to_csv(
    #     'D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\comparisonWithGroundTruth.csv', index=False)
    # print("FINISHED")
