# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        root = prev = ListNode(1)
        
        root.next = head
        
        
        while prev.next and prev.next.next:
            cur = prev.next
            curNext = cur.next 
            
            cur.next = curNext.next
            curNext.next = cur
            prev.next = curNext
            
            prev = cur
            
        return root.next
            
            
