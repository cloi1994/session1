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
        
        cur = head
        
        newCur = root = RandomListNode(1)
        
        hm = {}
        
        
        
        while cur:
            newCur.next = RandomListNode(cur.label)
            hm[cur] = newCur.next
            cur = cur.next
            newCur = newCur.next

        cur = head
            
        while cur:
            if cur.random:
                hm[cur].random = hm[cur.random]
            cur = cur.next
            
        return root.next
