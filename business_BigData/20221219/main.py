from unDirectedGraph import unDirectedGraph
from DirectedGraph import DirectedGraph
from utils import manageFolder


if __name__ == "__main__":

    manageFolder('plots')
    manageFolder('tables')

    edgeData = [
        (2, 3), (3, 2), (4, 1), (4, 2),
        (5, 2), (5, 4), (5, 6), (6, 2),
        (6, 5), (7, 2), (7, 5), (8, 2),
        (8, 5), (9, 2), (9, 5), (10, 5), (11, 5)
    ]

    weightData = {
        1: [0.1, 0.9], 2: [0.4, 0.8], 3: [0.8, 0.9], 4: [0.15, 0.55],
        5: [0.5,  0.5], 6: [0.8,  0.5], 7: [0.22, 0.3], 8: [0.30, 0.27],
        9: [0.38, 0.24], 10: [0.7,  0.3], 11: [0.75, 0.35]
    }

    unDirectedGrapg1 = unDirectedGraph(
        edgeData,
        "edgeData.png",
        "./tables/edgeData_unDirectedGraphInfo.csv"
    )
    unDirectedGrapg1.draw_degree_centrality()
    unDirectedGrapg1.draw_eigenvector_centrality()
    unDirectedGrapg1.draw_closeness_centrality()
    unDirectedGrapg1.draw_betweenness_centrality()
    unDirectedGrapg1.draw_clustering()
    unDirectedGrapg1.draw_katz()
    unDirectedGrapg1.graphData()

    directedGrapg1 = DirectedGraph(
        edgeData,
        weightData,
        "./tables/edgeData_directedGraphDegreeInfo.csv"
    )
    directedGrapg1.getDegreeInfo()
    directedGrapg1.draw_pageRank()
