# Definition for singly-linked list.
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