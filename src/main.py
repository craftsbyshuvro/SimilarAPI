from src.model.CombinedModel import CombinedModel
from src.model.SkipGram import SkipGram
from src.model.TFIDVect import TFIDVect

if __name__ == '__main__':
    # input_data = {'source_api_name_fully_qualified': 'com.google.common.base.Joiner:on()',
    #               'source_api_description': 'Returns a joiner which automatically places separator between consecutive elements.',
    #               'target_api_name_fully_qualified': 'org.apache.commons.lang.StringUtils:join()',
    #               'target_api_description': 'splits a String into an array of substrings and vice versa'
    #               }

    input_data = {'source_api_name_fully_qualified': 'com.google.gson.JsonObject:has()',
                  'source_api_description': 'param enabl',
                  'target_api_name_fully_qualified': 'org.apache.commons.lang.StringUtils:join()',
                  'target_api_description': 'param view'
                  }

    obj_combined_performance = CombinedModel()
    overall_similarity = obj_combined_performance.get_combined_performance(input_data)

    print('Source: ', input_data['source_api_name_fully_qualified'])
    print('Source: ', input_data['target_api_name_fully_qualified'])
    print('Similarity: ', overall_similarity)
