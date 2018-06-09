# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if not lists:
            return []
        
        return self.mergeSort(lists,0,len(lists)-1)
    
    def mergeSort(self,lists,start,end):
        
        if start >= end:
            return lists[start]
        
        mid = start + (end - start) // 2
        
        left = self.mergeSort(lists,start,mid)
        right = self.mergeSort(lists,mid+1,end)
        
        return self.merge(left,right)
    
    def merge(self,l1,l2):
        
        dummy = cur = ListNode(1)
        
        
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
        
        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2
            
        
        
        return dummy.next
        
        
        
        
        
