# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            dummy = ListNode(0)
            curr = dummy
            while list1 and list2:
                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next
            curr.next = list1 if list1 else list2
            return dummy.next
        if not lists or len(lists) == 0:    return None
        while len(lists) > 1:
            mergedLists = []
            for i in range((len(lists) + 1) // 2):
                l1 = lists[i]
                l2 = lists[len(lists) - i - 1] if i != len(lists) - i - 1 else None
                mergedLists.append(merge2Lists(l1,l2))
            lists = mergedLists
        return lists[0]
            