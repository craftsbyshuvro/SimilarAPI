import pickle
import networkx as nx
import matplotlib.pyplot as plt
from graph_tools import Graph
from pecanpy.pecanpy import SparseOTF
from tqdm import tqdm

from src.preprocess.DataPreprocess import DataPreprocess
import itertools
from karateclub import DeepWalk, Node2Vec
from scipy import spatial

class GraphEmbed:

    def embed(self):

        obj_preprocess = DataPreprocess()
        api_call_sequence = obj_preprocess.preprocess_api_call_sequence()
        invoked_methods_sentences = list(api_call_sequence['invoked_method'])

        print('encoding start')
        # Label encode
        invoked_methods_sentences = self.encode_unique_label(invoked_methods_sentences)

        print('encoding finished')

        G = self.build_graph(invoked_methods_sentences)

        ss = G.edges(data=True)
        # print(ss)


        nx.write_gpickle(G, 'D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\graph.gpickle')
        print('graph dumpped')

        edge_list_file = "D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\graphedzz.edgelist"

        nx.write_edgelist(G, edge_list_file)

        g = SparseOTF(p=1, q=1, workers=1, verbose=False)
        g.read_edg(edge_list_file, weighted=False, directed=False, delimiter=' ')

        # generate random walks
        walks = g.simulate_walks(num_walks=10, walk_length=80)
        # use random walks to train embeddings
        a= 100

        # self.plot_graph(G)

        # self.analyze_graph()

    def encode_unique_label(self, sentences):
        identifiers = {}
        idx = 0
        for sent in sentences:
            for word in sent.split():
                if word not in identifiers:
                    identifiers[word] = idx
                    idx += 1

        print(identifiers)

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
