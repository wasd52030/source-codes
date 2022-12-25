from typing import List, Tuple
import networkx
import pandas
from matplotlib import pyplot
from utils import Logger


class unDirectedGraph():
    def __init__(self, nodeData: List[Tuple[int, int]], pic_name: str, graph_info_path: str) -> None:
        self.graph: networkx.Graph = networkx.Graph()
        if nodeData != None:
            self.graph.add_edges_from(nodeData)
        self.base_pic_name: str = pic_name
        self.graph_info_path: str = graph_info_path
        self.spring_layout = networkx.spring_layout(self.graph, seed=555)
        self.SNA = dict(
            DEGREE=dict(self.graph.degree()),
            DEGREE_CENTRALITY=networkx.degree_centrality(self.graph),
            EIGENVECTOR=networkx.eigenvector_centrality_numpy(self.graph),
            KATZ=networkx.katz_centrality(self.graph),
            CLOSENESS_CENTRALITY=networkx.closeness_centrality(self.graph),
            BETWEENNESS_CENTRALITY=networkx.betweenness_centrality(self.graph),
            CLUSTCOEF=networkx.clustering(self.graph)
        )

        # 為了取得Class name，放棄語法糖改採原始方式
        self.draw_degree_centrality = (
            Logger(self.__class__.__name__)(self.draw_degree_centrality)
        )
        self.draw_eigenvector_centrality = (
            Logger(self.__class__.__name__)(self.draw_eigenvector_centrality)
        )
        self.draw_closeness_centrality = (
            Logger(self.__class__.__name__)(self.draw_closeness_centrality)
        )
        self.draw_betweenness_centrality = (
            Logger(self.__class__.__name__)(self.draw_betweenness_centrality)
        )
        self.draw_clustering = (
            Logger(self.__class__.__name__)(self.draw_clustering)
        )
        self.draw_katz = (
            Logger(self.__class__.__name__)(self.draw_katz)
        )
        self.graphData = Logger(self.__class__.__name__)(self.graphData)

    def setPicName(self, methodName: str):
        return self.base_pic_name.replace(self.base_pic_name.split('.')[0], self.base_pic_name.split('.')[0]+f'_{methodName}')

    def draw_degree_centrality(self):
        measures = self.SNA['DEGREE_CENTRALITY']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            self.spring_layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            self.spring_layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, self.spring_layout)
        pyplot.title('degree_centrality')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('DEGREE_CENTRALITY')}"
        )
        pyplot.cla()
        pyplot.clf()

    def draw_eigenvector_centrality(self):
        measures = self.SNA['EIGENVECTOR']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            self.spring_layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            self.spring_layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, self.spring_layout)
        pyplot.title('eigenvector_centrality')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('eigenvector_centrality'.upper())}"
        )
        pyplot.cla()
        pyplot.clf()

    def draw_closeness_centrality(self):
        measures = self.SNA['CLOSENESS_CENTRALITY']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            self.spring_layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            self.spring_layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, self.spring_layout)
        pyplot.title('closeness_centrality'.upper())
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('closeness_centrality')}"
        )
        pyplot.cla()
        pyplot.clf()

    def draw_betweenness_centrality(self):
        measures = self.SNA['BETWEENNESS_CENTRALITY']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            self.spring_layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            self.spring_layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, self.spring_layout)
        pyplot.title('betweenness_centrality')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('betweenness_centrality'.upper())}"
        )
        pyplot.cla()
        pyplot.clf()

    def draw_clustering(self):
        layout = networkx.spring_layout(self.graph, seed=555)
        measures = self.SNA['CLUSTCOEF']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, layout)
        pyplot.title('clustering')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('clustering'.upper())}"
        )
        pyplot.cla()
        pyplot.clf()

    def draw_katz(self):
        layout = networkx.spring_layout(self.graph, seed=555)
        measures = self.SNA['KATZ']
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            layout,
            node_size=500,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            layout,
            font_family='SimHei',
            font_color="white"
        )
        networkx.draw_networkx_edges(self.graph, layout)
        pyplot.title('katz')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/{self.setPicName('katz'.upper())}"
        )
        pyplot.cla()
        pyplot.clf()

    def graphData(self):
        sna = pandas.DataFrame(self.SNA)
        sna = sna.sort_values(by=['DEGREE_CENTRALITY'], ascending=False)
        sna.to_csv(self.graph_info_path)
