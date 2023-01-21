# write tests for bfs
import pytest
import networkx as nx
from random import choice
import sys
import pathlib

PARENT_PARENT_FOLDER = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PARENT_PARENT_FOLDER))
from search import graph


def test_bfs_traversal():
    """
    unit test for a breadth-first traversal by comparing the function created in graph.py to
    networkx's equivalent function as a ground truth
    """
    tiny_network_file = PARENT_PARENT_FOLDER / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)
    random_node = choice(list(tiny_network.graph.nodes()))
    networkx_solution = nx.bfs_tree(tiny_network.graph, random_node)
    my_solution = tiny_network.bfs(random_node)
    assert list(networkx_solution) == my_solution


def test_bfs():
    """
    unit test for a breadth-first shortest path by comparing the function created in graph.py to
    networkx's equivalent function as a ground truth
    """
    tiny_network_file = PARENT_PARENT_FOLDER / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)
    random_node_1 = choice(list(tiny_network.graph.nodes()))
    random_node_2 = choice(list(tiny_network.graph.nodes()))
    networkx_all_solutions = nx.all_shortest_paths(tiny_network.graph, random_node_1, random_node_2)
    my_solution = tiny_network.bfs(random_node_1, random_node_2)
    assert my_solution in list(networkx_all_solutions)


def test_non_connected_nodes():
    """
    unit test that isolated nodes don't create a shortest path in the graph.py algorithm because no
    path exists
    """
    tiny_network_file = PARENT_PARENT_FOLDER / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)
    for _ in range(5):
        tiny_network.add_isolated_node()
    isolated_nodes = list(nx.isolates(tiny_network.graph))
    my_solution = tiny_network.bfs(choice(isolated_nodes))
    assert my_solution is None


def test_non_existent_start_node():
    """
    edge case #1

    unit test that attempting to create a shortest path with a non-existent start node with the
    graph.py algorithm raises a ValueError
    """
    tiny_network_file = PARENT_PARENT_FOLDER / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)
    random_node = choice(list(tiny_network.graph.nodes()))
    bad_node = tiny_network.find_non_existing_node()
    with pytest.raises(ValueError):
        tiny_network.bfs(bad_node, random_node)


def test_non_existent_end_node():
    """
    edge case #2

    unit test that attempting to create a shortest path with a non-existent end node with the
    graph.py algorithm raises a ValueError
    """
    tiny_network_file = PARENT_PARENT_FOLDER / "data" / "tiny_network.adjlist"
    tiny_network = graph.Graph(tiny_network_file)
    random_node = choice(list(tiny_network.graph.nodes()))
    bad_node = tiny_network.find_non_existing_node()
    with pytest.raises(ValueError):
        tiny_network.bfs(random_node, bad_node)
