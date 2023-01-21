#!/usr/bin/python3
"""

\brief
    This script is to debug the functions in graph.py
    Please don't grade this; it's not well formatted, and everything required for the rubric should
    be in graph.py and test_bfs.py
"""

import networkx as nx
import matplotlib.pyplot as plt
from random import choice

import search.graph as graph
import file_format

SHOW_PLOT = False


def main() -> None:
    tiny_network_file = file_format.find_current_python_folder() / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)

    random_node_1 = choice(list(tiny_network.graph.nodes()))
    random_node_2 = choice(list(tiny_network.graph.nodes()))
    print(list(nx.bfs_tree(tiny_network.graph, random_node_1)))  # bfs_edges and take 2nd index?
    print(tiny_network.bfs(random_node_1))
    print()
    print(list(nx.all_shortest_paths(tiny_network.graph, random_node_1, random_node_2)))
    print(tiny_network.bfs(random_node_1, random_node_2))
    print()

    large_network_file = file_format.find_current_python_folder() / "data" / \
                         "citation_network.adjlist"
    large_network = graph.Graph(large_network_file)
    for _ in range(5):
        large_network.add_isolated_node()
    print(list(nx.isolates(large_network.graph)))
    print(large_network.bfs(choice(list(nx.isolates(large_network.graph)))))

    if SHOW_PLOT:
        nx.draw_networkx(tiny_network.graph)
        plt.show()


if __name__ == "__main__":
    main()
