zclass Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute force approach using hashTable or sorting will result of Sc = O(n),Which REFUSED
        # Optimized, Floyd's Alg with slow/fast pointers: Tc = O(n), Sc = O(1)
        
        slow, fast = 0, 0 # pointers represent indecies, not array values

        #phase 1: find intersaction
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #phase 2: find entrance
        slow2 = 0  
        while True:
            slow = nums[slow] # where slow intersect with fast
            slow2 = nums[slow2] # start at beginning of array until it intersect with slow
            if slow == slow2:
                break
        return slow # always the beginning of a cycle

