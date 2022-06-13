# f = open("D:/Study/Final Project/Applications/SimilarAPI/src/temp/test.txt", 'a')
# f.write(str(word_tokenizer))
# f.close()

# print(tabulate(pre_processed_df, headers='keys', tablefmt='psql'))


# words = model_skip_gram.wv.most_similar(positive=['java.lang.String.equalsIgnoreCase'], topn=3)


# if np.all(source_api == 0) or np.all(target_api == 0):
#     print("ONE of those is zero")


# input_data = {'source_api_name_fully_qualified': 'org.apache.commons.io.IOUtils.readLines()',
#               'source_api_description': 'Gets the contents of an InputStream as a list of Strings, one entry per line, using the specified character encoding.',
#               'target_api_name_fully_qualified': 'com.google.common.io.CharStreams.readLines()',
#               'target_api_description': 'Reads all of the lines from a Readable object.'
#               }

# input_data = {'source_api_name_fully_qualified': 'org.apache.commons.io.FileUtils.writeStringToFile()',
#               'source_api_description': 'Writes a String to a file creating the file if it does not exist.',
#               'target_api_name_fully_qualified': 'com.google.common.io.Files.write()',
#               'target_api_description': 'Overwrites a file with the contents of a byte array.'
#               }

# input_data = {'source_api_name_fully_qualified': 'org.apache.commons.io.FileUtils.moveFile()',
#               'source_api_description': 'Moves a file.',
#               'target_api_name_fully_qualified': 'com.google.common.io.Files.move()',
#               'target_api_description': 'Moves a file from one path to another.'
#               }

# input_data = {'source_api_name_fully_qualified': 'org.apache.commons.lang.StringUtils.split()',
#               'source_api_description': 'Splits the provided text into an array with a maximum length, separators specified.',
#               'target_api_name_fully_qualified': 'com.google.common.base.Splitter.split()',
#               'target_api_description': 'Splits sequence into string components and makes them available through an Iterator, which may be lazily evaluated.'
#               }


# input_data = {'source_api_name_fully_qualified': 'org.apache.commons.io.FileUtils.moveFile()',
#               'source_api_description': 'Moves a file.',
#               'target_api_name_fully_qualified': 'com.google.common.io.Files.move()',
#               'target_api_description': 'Moves a file from one path to another.'
#               }
#
# obj_combined_performance = CombinedModel()
# overall_similarity = obj_combined_performance.get_combined_performance(input_data)
#
# print('Source: ', input_data['source_api_name_fully_qualified'])
# print('Target: ', input_data['target_api_name_fully_qualified'])
# print('Similarity: ', overall_similarity)

