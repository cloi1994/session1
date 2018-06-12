# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        
        root = cur = ListNode(1)
        
        while carry or l1 or l2:
            summ = carry
            if l1:
                summ  += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            
            carry = summ / 10 
            summ = summ % 10
            
            cur.next = ListNode(summ)
            cur = cur.next
            
        return root.next
                
            
                
                
        
