# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        hm = {}
        
        root = newcur = RandomListNode(1)
        
        cur = head
        
        while cur:
            newNode = RandomListNode(cur.label)
            hm[cur] = newNode
            
            cur = cur.next
        
            newcur.next = newNode
            newcur = newcur.next
            
        cur = head
        
        while cur:            
            if cur.random:
                hm[cur].random = hm[cur.random]
            cur = cur.next
            
        return root.next
        
        
        
        
        
        
        
        
        
