# Here I follow chaining approach to build a hashSet
class ListNode:
    def __init__(self,key = -1, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.map = [ ListNode() for i in range(1000)] # Initialize every Index with a dummy node 

    # Create this helper Fn bc we use its body in several parts in our code      
    def hash(self, key):
        return key % len(self.map)

    def add(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next: # here .next is to cover pointing in the last node, and in the statr there is a dummy node
            if cur.next.key == key: # If the key is alredy exists,Update val
                cur.next.key = key
                return 
            cur = cur.next
        cur.next = ListNode(key)    

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)] # here we start from dummy node bc we need to do some pointer manipulation
        while cur and cur.next:
            if cur.next.key == key: # Here .next bc I want to stop at the node prior to the node I want to remove
                cur.next = cur.next.next
                return 
            cur = cur.next   

    def contains(self, key: int) -> bool:
        cur = self.map[self.hash(key)].next # .next bc I don't want to check dummy node value
        while cur:
            if cur.key == key :
                return True
            cur = cur.next
        return        



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
