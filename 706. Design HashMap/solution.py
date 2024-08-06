# Here I follow chaining approach to build a hashMap
class ListNode:
    def __init__(self,key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next
        
class MyHashMap:
    # Initialize every Index with a dummy node ,AND here we have fixed capacity we don't do rehashing
    def __init__(self):
        self.map = [ ListNode() for i in range(1000)]    

    # Create this helper Fn bc we use its body in several parts in our code      
    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next: # here .next is to cover pointing in the last node, and in the statr there is a dummy node
            if cur.next.key == key: # If the key is alredy exists,Update val
                cur.next.val = value
                return 
            cur = cur.next
        cur.next = ListNode(key,value)    

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next # .next bc I don't want to check dummy node value
        while cur:
            if cur.key == key :
                return cur.val
            cur = cur.next
        return -1        

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)] # here we start from dummy node bc we need to do some pointer manipulation
        while cur and cur.next:
            if cur.next.key == key: # Here .next bc I want to stop at the node prior to the node I want to remove
                cur.next = cur.next.next
                return 
            cur = cur.next                

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
