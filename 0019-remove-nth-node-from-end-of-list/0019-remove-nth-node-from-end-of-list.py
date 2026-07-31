# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        cnt = 0
        while fast and cnt <= n:
            fast = fast.next
            cnt += 1
        while fast:
            fast = fast.next
            slow = slow.next
        erase = slow.next
        keep = erase.next
        slow.next = keep
        return dummy.next