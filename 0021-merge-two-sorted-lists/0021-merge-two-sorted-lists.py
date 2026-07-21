# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            p = ListNode(list2.val)
            p.next = self.mergeTwoLists(list1, list2.next)
        elif not list2:
            p = ListNode(list1.val)
            p.next = self.mergeTwoLists(list1.next, list2)
        elif list1.val >= list2.val:
            p = ListNode(list2.val)
            p.next = self.mergeTwoLists(list1, list2.next)
        else:
            p = ListNode(list1.val)
            p.next = self.mergeTwoLists(list1.next, list2)
        return p
        