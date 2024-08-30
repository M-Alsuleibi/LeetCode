class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Monotonic Stack : Tc = O(n)
        
        ans = [-1] * len(nums1)
        dic = {num: i for i, num in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                ans[dic[val]] = curr
            if curr in dic:
                stack.append(curr)
        return ans

