from typing import Dict, List, Tuple
import networkx
import pandas
from matplotlib import pyplot
from utils import Logger


class DirectedGraph:
    def __init__(self, nodeData: List[Tuple[int, int]], dpos: Dict[int, List[float]], graph_info_path: str) -> None:
        self.graph: networkx.DiGraph = networkx.DiGraph()
        self.graph.add_edges_from(nodeData)

        self.dpos: Dict[int, List[int]] = dpos

        self.graph_info_path: str = graph_info_path

        self.getDegreeInfo = (
            Logger(self.__class__.__name__)(self.getDegreeInfo)
        )
        self.draw_pageRank = (
            Logger(self.__class__.__name__)(self.draw_pageRank)
        )

    def getDegreeInfo(self):
        data = pandas.DataFrame({
            'in_degrees'.upper(): self.graph.in_degree(),
            'out_degrees'.upper(): self.graph.out_degree()
        })
        data.to_csv(self.graph_info_path)

    def draw_pageRank(self):
        measures = networkx.pagerank(self.graph, alpha=0.85)
        nodes = networkx.draw_networkx_nodes(
            self.graph,
            self.dpos,
            node_size=500,
            cmap=pyplot.cm.plasma,
            node_color=[*measures.values()],
            nodelist=measures.keys()
        )
        networkx.draw_networkx_labels(
            self.graph,
            self.dpos,
            font_color="white",
            font_size=12
        )
        networkx.draw_networkx_edges(self.graph, self.dpos)
        pyplot.title('Directed graph pageRank')
        pyplot.colorbar(nodes)
        pyplot.axis('off')
        pyplot.savefig(
            f"./plots/edgeData_directedGraphPageRank.png"
        )
        pyplot.cla()
        pyplot.clf()
