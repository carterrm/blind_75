# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    next = curr

    while next is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# def detect_cycle(head):
#     #This solution is fast (beats 72%), but uses a lot of memory (beats 5.7%).
#     check_set = set()
#     if head is None or head.next is None:
#         return False
#     while True:
#         if head.next is None:
#             return False
#         elif head.next in check_set:
#             return True
#         else:
#             check_set.add(head.next)
#             head = head.next

def detect_cycle(head):
    #This solution is much faster, requiring only 3 more ms to run (still beats 53%) while using .5 mb less memory (beats 83%)
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if slow.next is None or fast.next is None:
            return False
        elif fast.next.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #This solution beats 93.64% on runtime and 52.93% on memory usage
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    current = None
    #Set the starting point
    if list1.val <= list2.val:
        current = list1
        list1 = list1.next
    elif list2.val < list1.val:
        current = list2
        list2 = list2.next
    merged_head = current

    while list1 is not None or list2 is not None:
        if list1 is not None and (list2 is None or list1.val <= list2.val):
            current.next = list1
            list1 = list1.next
        elif list2 is not None and (list1 is None or list2.val < list1.val):
            current.next = list2
            list2 = list2.next
        current = current.next
    return merged_head

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #Beats 40.97% on runtime, 94.80% on memory usage
    if head.next is None:
        return None
    count = 0
    temp = head
    while temp is not None:
        temp = temp.next
        count += 1

    if n == count:
        return head.next

    temp = head
    rear = None
    front = None
    for i in range(1, count - n):
        temp = temp.next

    rear = temp
    front = temp.next
    if front is not None:
        front = front.next
    rear.next = front
    return head

def reorder_list(head) -> None:
    #Not fast (5.02%), but good on memory (65.71%)!
    #Edge cases
    if head.next is None:
        return head
    #Add nodes to list
    temp = head
    node_list = []
    while temp is not None:
        node_list.append(temp)
        temp = temp.next
    #Now we have the full list of nodes
    list_size = len(node_list)
    for i in range (1, list_size, 2):
        if i % 2 == 1:
            #node_list[ list_size - 1] is to be inserted at i * 2 - 1 len(node_list) - i
            node_list.insert((i),node_list[list_size - 1])
            node_list.pop()
            #Make the swap in the linked list
            node_list[i - 1].next = node_list[i]
            if i < list_size - 1:
                node_list[i].next = node_list[i + 1]
            node_list[list_size - 1].next = None

    #No extra space solution: Usually pretty good on runtime & memory, but occasionally super sucky on both.
    # head_copy = head
    # fast = head
    # slow = head
    # if head.next is None:
    #     return head
    # while fast.next is not None:
    #     fast = fast.next
    #     if fast is not None and fast.next is not None:
    #         fast = fast.next
    #         slow = slow.next
    #
    #
    # #Slow is now at the end of the first half of the list
    # second = slow.next
    # prev = slow.next = None
    # while second is not None:
    #     temp = second.next
    #     second.next = prev
    #     prev = second
    #     second = temp
    #
    # first, second = head, prev
    #
    # while second is not None:
    #     temp_1, temp_2 = first.next, second.next
    #     first.next = second
    #     second.next = temp_1
    #     first, second = temp_1, temp_2
    #     second = temp_2

