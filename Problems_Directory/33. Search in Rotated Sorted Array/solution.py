class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Forcce: Tc O(n), Sc O(1)
        #for i in range(len(nums)):
        #    if nums[i] == target :
        #        return i    
        #return -1    
        #-----------------------------------------------------

        #Optimized: Binary Search for circularly sorted array
        # Tc = O(logn) , Sc = O(1)
        L, R = 0, len(nums) - 1 
        while L <= R:
            mid = (L+R) // 2
            #case 1
            if nums[mid] == target:
                return mid
            #case 2    
            if nums[mid] <= nums[R]:
                if target >= nums[mid] and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            #case 3
            if nums[mid] >= nums[L]:
                if target <= nums[mid] and target >= nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1                 
