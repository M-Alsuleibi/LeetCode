# [1985. Find the Kth Largest Integer in the Array](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/) `MEDIUM`
## Intuition
My first thoughts might involve converting the strings to integers, sorting them in descending order, and then selecting the kth largest number.

## Approach
1. Convert the list of strings nums to a list of integers.
2. Sort the list of integers in descending order.
3. Return the kth largest number from the sorted list.

## Complexity
- Time complexity:
	- Converting the list of strings to a list of integers takes O(n) time, where n is the number of elements in the list.
	- Sorting the list of integers takes O(n log n) time using Python's built-in sorting algorithm, which is typically Timsort.
	- Accessing the kth largest number from the sorted list takes O(1) time.
 Therefore, the overall time complexity is `O(n log n)` due to the sorting operation.

- Space complexity:
	- Converting the list of strings to a list of integers requires additional space proportional to the size of the input list, resulting in O(n) space complexity.
	- Sorting the list of integers does not require additional space as it's performed in-place.
Overall, the space complexity is `O(n)` due to the additional space needed for the integer conversion.

