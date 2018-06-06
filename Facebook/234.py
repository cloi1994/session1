# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return True
        
        s = []
        
        
        slow = head
        fast = head.next  # fast.next for mid to separate odd and even length
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        left = head
        right = slow.next
        right = self.reverse(right)
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
    
    def reverse(self,cur):
        
        pre = None
        
        while cur:
            curNext = cur.next
            cur.next = pre
            pre = cur
            cur = curNext
        
        return pre
        
            
