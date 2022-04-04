from src.model.CombinedModel import CombinedModel
from src.model.TrainModels import TrainModel

if __name__ == '__main__':

    obj_train_model = TrainModel()

    # obj_train_model.train_skip_gram()
    # obj_train_model.embed_method_name()
    # obj_train_model.embed_method_api_name()
    # obj_train_model.embed_method_comment()

    input_data = {'source_api_name_fully_qualified': 'com.google.common.base.Joiner:on()',
                  'source_api_description': 'Returns a joiner which automatically places separator between consecutive elements.',
                  'target_api_name_fully_qualified': 'org.apache.commons.lang.StringUtils:join()',
                  'target_api_description': 'splits a String into an array of substrings and vice versa'
                  }

    obj_combined_performance = CombinedModel()
    overall_similarity = obj_combined_performance.get_combined_performance(input_data)

    print('Source: ', input_data['source_api_name_fully_qualified'])
    print('Target: ', input_data['target_api_name_fully_qualified'])
    print('Similarity: ', overall_similarity)