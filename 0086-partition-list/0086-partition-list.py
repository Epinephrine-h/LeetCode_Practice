# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bigDummy = ListNode(0)
        smallDummy = ListNode(0)
        bPtr, mPtr = bigDummy, smallDummy
        cur = head
        while cur:
            if cur.val < x:
                mPtr.next = cur
                mPtr = mPtr.next
            else:
                bPtr.next = cur
                bPtr = bPtr.next
            cur = cur.next
        bPtr.next = None
        mPtr.next = bigDummy.next
        return smallDummy.next
                

