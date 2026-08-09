# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt += 1
        half = cnt // 2
        ptr = 0
        ans = head
        while ptr < half:
            ans = ans.next
            ptr += 1
        return ans