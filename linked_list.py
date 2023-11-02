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
