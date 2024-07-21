class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
         # Convert the list of strings to a list of integers
         nums_int = [int(num) for num in nums]
         
         # Sort the list of integers in descending order
         nums_int.sort(reverse=True)
         
         # Return the kth largest number converted back to string
         return str(nums_int[k - 1])

