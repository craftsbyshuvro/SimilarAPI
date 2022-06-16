import pickle
import networkx as nx
import matplotlib.pyplot as plt
from src.preprocess.DataPreprocess import DataPreprocess
import itertools


class GraphEmbed:

    def embed(self):

        # self.analyze_graph()

        obj_preprocess = DataPreprocess()
        api_call_sequence = obj_preprocess.preprocess_api_call_sequence()
        invoked_methods_sentences = list(api_call_sequence['invoked_method'])

        print('encoding start')
        # Label encode
        invoked_methods_sentences = self.encode_unique_label(invoked_methods_sentences)
        print('encoding finished')

        G = self.build_graph(invoked_methods_sentences)

        # ss = G.edges(data=True)
        # print(ss)

        nx.write_gpickle(G, 'D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\graph.gpickle')

        self.plot_graph(G)

        print('graph dumpped')

    def encode_unique_label(self, sentences):
        identifiers = {}
        idx = 0
        for sent in sentences:
            for word in sent.split():
                if word not in identifiers:
                    identifiers[word] = idx
                    idx += 1
        list_values = []
        for sent in sentences:
            values = [str(identifiers[word]) for word in sent.split()]
            str_values = " ".join(values)
            list_values.append(str_values)
        return list_values

    def analyze_graph(self):
        G = nx.read_gpickle('D:\Study\Final Project\Dataset\Ground Truth\GoogleLangCommonLang\graph.gpickle')
        sim = nx.simrank_similarity(G, '0', '1')
        print('graph simlarity')
        print(sim)

    def get_node_relation_custom(self, document):
        mapped_pairs = []
        for sent in document:
            split_str = sent.split(" ")
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
        print('nodes finished')

        print('edges  started')
        # get graph edges
        # edges = self.get_relations(document)
        edges = self.get_node_relation_custom(document)
        print('edges  finished')

        # create graph structure with NetworkX
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        return G

    def get_entities_custom(self, document):
        unique_words = set(itertools.chain.from_iterable(map(str.split, document)))
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
        for sent in document:
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
