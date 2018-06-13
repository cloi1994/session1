class Node(object):
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v

class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0) # head is a dummy head node
        self.tail = Node(0, 0) # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_tail(self):
        old_tail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return old_tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dll = DoublyLinkedList()
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            val = node.val
            self.dll.remove_node(node)
            newNode = Node(key,val)
            self.cache[key] = newNode
            self.dll.add_to_head(newNode)
            return newNode.val
        
        
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            self.dll.remove_node(node)
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.dll.add_to_head(newNode)
        else:
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.dll.add_to_head(newNode)
            
            if len(self.cache) > self.capacity:
                old_tail = self.dll.remove_tail()
                self.cache.pop(old_tail.key)
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
