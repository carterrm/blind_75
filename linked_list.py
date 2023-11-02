# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     if head == None:
#         return None
#     if head.next == None:
#         #Base case- this is the last node in your list. Return it to start going back up.
#         return head
#     else:
#         new_head = reverseList(head.next)
#         focus_node = new_head
#         while focus_node.next != None:
#             focus_node = focus_node.next
#         focus_node.next = head
#         focus_node.next.next = None
#         return new_head

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
