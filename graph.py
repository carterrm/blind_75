# Definition for a Node.
import copy
from typing import Optional


class graph_node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs(start_node, node_map):  #TODO in leetcode, you must add self as an argument to dfs() and call it as self.dfs
    start_node_clone = None
    #for current node:
    #clone it if not already cloned
    if start_node not in node_map:
        start_node_clone = graph_node(start_node.val)   #TODO in Leetcode, switch graph_node for Node to match the test's class name
        node_map[start_node] = start_node_clone
    else:
        start_node_clone = node_map[start_node]
    #add original & clone to map
    #for each neighbor, call dfs on it
    for neighbor in start_node.neighbors:
        if neighbor not in node_map:
            cloned_neighbor = dfs(neighbor, node_map)
        else:
            cloned_neighbor = node_map[neighbor]
        # after dfs returns (so we know neighbor has been cloned),
        # add cloned-neighbor to cloned-original's neighbor list
        start_node_clone.neighbors.append(cloned_neighbor)
        # return cloned original
    return start_node_clone



def clone_graph(node: Optional['graph_node']) -> Optional['graph_node']:
    if node is None:
        return None
    node_map = {}
    start_node_copy = dfs(node, node_map)
    return start_node_copy



