import json
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from graph_tools import Graph
from pecanpy.pecanpy import SparseOTF, DenseOTF
from tqdm import tqdm

from src.config import AppConfig
from src.preprocess.DataPreprocess import DataPreprocess
import itertools
from karateclub import DeepWalk, Node2Vec
from scipy import spatial
import joblib


class GraphEmbed:
    def __init__(self):
        self.graph_edge_path = 'saved_model/graphedge.edgelist'
        self.embeddingsSize = 300
        self.dict_map_number = 'saved_model/dege_str_number.txt'

    def embed(self):
        obj_preprocess = DataPreprocess()
        api_call_sequence = obj_preprocess.preprocess_api_call_sequence()
        invoked_methods_sentences = list(api_call_sequence['invoked_method'])

        invoked_methods_sentences = self.encode_unique_label(invoked_methods_sentences)

        G = self.build_graph(invoked_methods_sentences)

        nx.write_edgelist(G, self.graph_edge_path)

        print('edge has been written to file')

        print('embedding started')
        self.save_graph_embed_model()

        # self.get_api_seq_similarity()

        # self.plot_graph(G)
        # self.analyze_graph

    def get_api_seq_similarity(self):

        skip_gram_model = Word2Vec.load(AppConfig.GRAPH_EMBEDD_MODEL_PATH_API_SEQ)

        dict_data = ''
        with open(self.dict_map_number) as f:
            dict_data = f.read()

        # reconstructing the data as a dictionary
        dict_mapping = json.loads(dict_data)
        sss = dict_mapping['org.apache.commons.io.IOUtils.readLines()']

        # print(skip_gram_model.wv.index_to_key)
        print(skip_gram_model.wv.similar_by_word('40010', 20))

        # source_api_vector = skip_gram_model.wv['0']
        # target_api_vector = skip_gram_model.wv['6']
        #
        # cosine_similarity = 1 - spatial.distance.cosine(source_api_vector, target_api_vector)
        #
        # print('similarity:  ', cosine_similarity)
        #
        # return cosine_similarity

    def get_api_seq_similarity(self, input_data, model_vect = None ,dic_data = None,):

        if model_vect is None:
            skip_gram_model = Word2Vec.load(AppConfig.GRAPH_EMBEDD_MODEL_PATH_API_SEQ)
        else:
            skip_gram_model = model_vect

        # skip_gram_model = Word2Vec.load(AppConfig.GRAPH_EMBEDD_MODEL_PATH_API_SEQ)

        source_api = input_data['source_api_name_fully_qualified_raw']
        target_api = input_data['target_api_name_fully_qualified_raw']

        # skip_gram_model = Word2Vec.load(AppConfig.SKIP_GRAM_MODEL_PATH_API_SEQ)

        dict_data = ''
        if dic_data is None:
            with open(self.dict_map_number) as f:
                dict_data = f.read()
        else:
            dict_data = dic_data

        # reconstructing the data as a dictionary
        dict_mapping = json.loads(dict_data)

        source_api = dict_mapping[source_api]
        target_api = dict_mapping[target_api]

        similarity = skip_gram_model.wv.similarity(source_api, target_api)

        return similarity

    def save_graph_embed_model(self):
        g = SparseOTF(p=1, q=1, workers=1, verbose=False)

        # Reading edges from file
        g.read_edg(self.graph_edge_path, weighted=False, directed=False, delimiter=' ')

        print('Walk Started')
        # generate random walks
        walks = g.simulate_walks(num_walks=12, walk_length=70)

        # print(walks)

        # use random walks to train embeddings
        # model_skip_gram = Word2Vec(walks, vector_size=8, window=3, min_count=0, sg=1, workers=1, epochs=1)

        model_skip_gram = Word2Vec(walks, window=5, min_count=1, workers=4, vector_size=self.embeddingsSize)

        # Saving model in file
        model_skip_gram.save(AppConfig.GRAPH_EMBEDD_MODEL_PATH_API_SEQ)

        print('Graph embedding Model trained and saved successfully')

    def encode_unique_label(self, sentences):
        identifiers = {}
        idx = 0
        for sent in sentences:
            for word in sent.split():
                if word not in identifiers:
                    identifiers[word] = idx
                    idx += 1

        # convert dictionary into string
        str_int_map = json.dumps(identifiers)
        with open(self.dict_map_number, 'w') as file:
            file.write(str_int_map)

        list_values = []
        for sent in sentences:
            values = [identifiers[word] for word in sent.split()]
            list_values.append(values)
        return list_values

    def analyze_graph(self):
        G = nx.read_gpickle('D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\graph.gpickle')

        # ss = G.edges(data=True)
        # print(ss)

        sim = nx.simrank_similarity(G, 1, 56)
        print('graph similarity', sim)
        print(sim)

        # model = DeepWalk()  # node embedding algorithm
        # model = DeepWalk(window_size=4)  # node embedding algorithm
        # model.fit(G)  # fit it on the graph
        # embedding = model.get_embedding()  # extract embeddings
        #
        # print('Number of karate club members:', len(G.nodes))
        # print('Embedding array shape:', embedding.shape)
        #
        # cosine_similarity = 1 - spatial.distance.cosine(embedding[4], embedding[i])
        # print(i, "   ", cosine_similarity)

        a = 9

    def get_node_relation_custom(self, document):
        mapped_pairs = []
        for sent in document:
            split_str = sent
            if len(split_str) == 0 or len(split_str) == 1:
                continue
            if len(split_str) == 2:
                mapped_pairs.append([split_str[0], split_str[1]])
                continue

            for outer_word in split_str:
                for inner_word in split_str:
                    if outer_word != inner_word:
                        mapped_pairs.append([outer_word, inner_word])

        return mapped_pairs

    def build_graph(self, document):

        print('nodes started')
        # get graph nodes
        # nodes = self.get_entities(document)
        nodes = self.get_entities_custom(document)
        print('nodes finished', len(nodes))

        print('edges  started')
        # get graph edges
        # edges = self.get_relations(document)
        edges = self.get_node_relation_custom(document)
        print('edges  finished', len(edges))

        # create graph structure with NetworkX
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        return G

    def get_entities_custom(self, document):
        unique_words = {x for l in document for x in l}
        return unique_words

    def get_entities(self, document):
        # in our case, entities are all unique words
        unique_words = []
        for sent in document:
            for word in sent.split(" "):
                if word not in unique_words:
                    unique_words.append(word)
        return unique_words

    def get_relations(self, document):
        # in our case, relations are bigrams in sentences
        bigrams = []
        for sent in tqdm(document):
            sent = sent.split(" ")
            for i in range(len(sent) - 1):
                # for every word and the next in the sentence
                pair = [sent[i], sent[i + 1]]
                # only add unique bigrams
                if pair not in bigrams:
                    bigrams.append(pair)
        return bigrams

    def plot_graph(self, G, title=None):
        # set figure size
        plt.figure(figsize=(10, 10))

        # define position of nodes in figure
        pos = nx.nx_agraph.graphviz_layout(G)

        # draw nodes and edges
        nx.draw(G, pos=pos, with_labels=True)

        # get edge labels (if any)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        # draw edge labels (if any)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # plot the title (if any)
        plt.title(title)

        plt.show()
