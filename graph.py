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


def course_schedule_dfs(head, adj_list, current_chain):
    if head in current_chain:
        return -1
    else: current_chain.add(head)
    delete_list = []
    for req in adj_list[head]:
        req_result = course_schedule_dfs(req, adj_list, current_chain)
        if req_result == -1:
            return -1
        else:
            delete_list.append(req_result)
    for index in delete_list:
        adj_list[head].remove(index)
    current_chain.remove(head)
    return head

def course_schedule(numCourses, prerequisites) -> bool:
    #This one was hard. This solution is very bad on memory, but on average is very fast!
    if len(prerequisites) == 0:
        return True
    adj_list = {}
    #make the adjacency list
    for i in range(0, numCourses):
        adj_list[i] = []
    for req in prerequisites:
        adj_list[req[0]].append(req[1])
    #DFS each node in the adjacency list
    for req in adj_list.keys():
        if adj_list[req] != []:
            if course_schedule_dfs(req, adj_list, set()) == -1:
                return False
    return True
