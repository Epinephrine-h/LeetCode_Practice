# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:   return head
        lenList = 0
        cur = head
        while cur:
            lenList += 1
            cur = cur.next
        k = k % lenList
        slow = fast = head
        dummy = ListNode(0, head)
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        dummy.next = slow.next
        slow.next = None
        return dummy.next
        