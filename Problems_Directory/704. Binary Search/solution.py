class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time complexity = O(log n ), while n is the length of the input arrary

        L , R = 0 , len(nums) - 1

        while L <= R : 
            mid = (L + R) // 2

            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid
        return -1      
