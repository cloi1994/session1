# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        aLen = self.getLength(headA)
        bLen = self.getLength(headB)
        
        
        n = abs(aLen - bLen)
        
        if aLen > bLen:
            
            while aLen > bLen:
                headA = headA.next
                aLen -= 1
            
        elif bLen > aLen:
            while bLen > aLen:
                headB = headB.next
                bLen -= 1
            
        
            
        while headA and headB:
            
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
            n -= 1
        
            
        return None
            
        
        
    def getLength(self,head):
        
        count = 0
        
        while head:
            head = head.next
            count += 1
        return count
        
