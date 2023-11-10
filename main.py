# This is a sample Python script.
import array
from array import *
from dynamic_programming import *
from linked_list import *
from graph import *
from binary import *

# Just to be clear, TODOs are only labeled as such so the font shows up in a different color. Nothing is actually still left to do.
if __name__ == '__main__':
    #TODO -- ARRAY PROBLEMS
    #two_sum_result = two_sum([3,2,4], 6)
    #buy_sell_stock_result = buy_sell_stock([7,1,5,3,6,4])
    #contains_duplicate_result = contains_duplicate([1,2,3,4,1])
    #product_except_self_result = product_except_self([1,2,3,4])
    #maximum_subarray_result = maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])
    #maximum_product_subarray_result = maximum_product_subarray([2,-5,-2,-4,3])
    #three_sum_result = three_sum([-2,0,1,1,2])

    #TODO -- BINARY PROBLEMS
    number_of_1_bits_result = number_of_1_bits(9)

    one = 1
    #TODO -- DYNAMIC PROGRAMMING PROBLEMS
    #climbing_stairs_result = climbing_stairs(5)
    #coin_change_result = coin_change([186,419,83,408], 6249)

    # TODO -- LINKED LIST PROBLEMS

    node_5 = ListNode(5)
    node_4 = ListNode(4,node_5)
    node_3 = ListNode(3,node_4)
    node_2 = ListNode(2)
    node_1 = ListNode(1, node_2)
    #reverse_linked_list_result = reverseList(node_1)

    # node_3 = ListNode(4, None)
    # node_2 = ListNode(2, node_3)
    # node_1 = ListNode(0, node_2)
    #
    # alt_node_3 = ListNode(5, None)
    # alt_node_2 = ListNode(3, alt_node_3)
    # alt_node_1 = ListNode(1, alt_node_2)

    #detect_cycle_result = detect_cycle(node_1)
    #mergeTwoLists_result = mergeTwoLists(node_1, alt_node_1)
    removeNthFromEndResult = removeNthFromEnd(node_1, 2)

    #TODO -- GRAPH PROBLEMS

    adj_list = []
    graph_node_1 = graph_node(1)
    graph_node_2 = graph_node(2)
    graph_node_3 = graph_node(3)
    graph_node_4 = graph_node(4)
    graph_node_5 = graph_node(5)
    graph_node_1.neighbors = [graph_node_2, graph_node_4]
    graph_node_2.neighbors = [graph_node_1, graph_node_3]
    graph_node_3.neighbors = [graph_node_2, graph_node_4]
    graph_node_4.neighbors = [graph_node_1, graph_node_3]

    #clone_graph_result = clone_graph(graph_node_1)
    three = 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
