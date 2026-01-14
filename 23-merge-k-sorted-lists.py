import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, n = heapq.heappop(heap)
            curr.next = n
            curr = curr.next

            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
            
        return dummy.next
