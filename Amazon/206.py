# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
    
        prev = None
        
        cur = head
        
        while cur:
            
            newNode = ListNode(cur.val)
            
            newNode.next = prev
            
            prev = newNode
            
            cur = cur.next
        
        return prev
    
        # 1 2 3
        # 
        # None <- 1 
