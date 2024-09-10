class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute Force: Tc = O(n), Sc = O(1)
        # minElemnt = nums[0]
        # for num in nums:
        #     if num < minElemnt:
        #         minElemnt = num
        # return minElemnt
        # ------------------------------------
        # Optimized: using a variation of Binary Search to find the minimum(Pivot) in 
        # circularly sorted array with condition :All the integers of the array are unique.
        # Tc = O(nlogn), Sc = O(1)
        # The equality in each comparison to cover cases such that [2,1] , where mid = L or  mid = prev for example.
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L+R) // 2
            #case 1
            # adding = with < to cover a single elemnt array case
            if nums[L] <= nums[R]:
                return nums[L]
            # prev = mid -1    
            prev, next = (mid + len(nums) - 1) % len(nums), (mid + 1) % len(nums)
            #case 2
            if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
                return nums[mid]
            #case 3
            elif nums[mid] >= nums[L]:
                L = mid + 1 
            elif nums[mid] <= nums[R]:
                R = mid - 1           

