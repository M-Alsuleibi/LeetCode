class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Initialize the result list with -1 for each element.
        result = [-1] * n

        # Stack to keep indexes of nums for which we haven't found the next greater element.
        stack = []

        # Iterate over the list twice to simulate circular array behavior.
        for i in range(2 * n): # Shorthand for n << 1.
            # Get the index in the original nums array.
            index = i % n

            # While stack is not empty and the current element is greater than the element at
            # the index of the last element in stack, update the result for the index at the
            # top of the stack.
            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]

            # For the first pass, we need to fill the stack with index.
            # Avoid pushing index onto the stack in the second pass to prevent duplicating work.
            if i < n:
                stack.append(index)

        # Return the result list containing next greater elements.
        return result
