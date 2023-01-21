import networkx as nx
import numpy as np
from typing import List, Union


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs_edges(self, current_node: Union[str, List], visited_nodes=None, visited_edges=None):
        """
        find edges in order of breadth-first search
        """
        if isinstance(current_node, list):
            queue = current_node
            current_node = queue[0]
        else:
            queue = [current_node]
        if visited_nodes is None:
            visited_nodes = [current_node]
        elif current_node not in visited_nodes:
            visited_nodes.append(current_node)
            queue.append(current_node)
        if visited_edges is None:
            visited_edges = []
        while queue:
            if current_node not in list(self.graph.nodes()):
                raise ValueError("start/current node given is not in the graph")
            neighbors = self.graph.neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited_nodes:
                    visited_nodes.append(neighbor)
                    visited_edges.append((current_node, neighbor))
                    queue.append(neighbor)
            queue.pop(0)
            if queue:
                self.bfs_edges(queue, visited_nodes, visited_edges)
        return visited_edges

    def bfs(self, start, end=None):
        """
        Performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of
        the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        bfs_edges = self.bfs_edges(start)
        if len(bfs_edges) == 0:
            return None
        bfs_edges_numpy_array = np.array(bfs_edges)
        path_ends = bfs_edges_numpy_array[:, 1].tolist()
        if end:
            if end not in list(self.graph.nodes()):
                raise ValueError("end node given is not in the graph")
            if start == end:
                return start
            else:
                if end in path_ends:
                    end_index = path_ends.index(end)
                    starting_node = bfs_edges_numpy_array[end_index, 0]
                    shortest_path = [starting_node, end]
                    while starting_node != start:
                        starting_node = bfs_edges_numpy_array[path_ends.index(starting_node), 0]
                        shortest_path.insert(0, starting_node)
                    return shortest_path
                else:
                    return None
        else:
            path_ends.insert(0, start)
            return path_ends

    def add_isolated_node(self):
        """
        add a non-connected node to the graph
        """
        new_node = self.find_non_existing_node()
        self.graph.add_node(new_node)

    def find_non_existing_node(self):
        """
        find a node that doesn't exist on the graph
        """
        i = 1
        while str(i) in list(self.graph.nodes()):
            i += 1
        return str(i)



