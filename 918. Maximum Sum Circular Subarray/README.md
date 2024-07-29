# [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/description/) `MEDIUM`
## Intution:
To solve the maximum subarray problem for a circular array, we must consider two cases:

1. The maximum sum subarray is similar to the one found in a non-circular array (Kadane's algorithm is useful here).
2. The maximum sum subarray is the result of wrapping around the circular array.
## Solution Approach:
1. Initialization
2. Iterate Over Array
3. Kadane’s Algorithm for Maximum Sum
4. Kadane’s Algorithm for Minimum Sum
5. Check for All Negative Elements: 
 If the globMax is non-positive, the whole array could be non-positive. Thus, the max subarray sum is the globMax itself
6. Find Maximum Sum Considering Circular Wrap :
Otherwise, we compare the globMax vs. total sum minus globMin. The latter represents the maximum sum obtained by considering the circular nature of the array. We subtract globMin from the total sum to get the maximum sum subarray which wraps around the array
7. Return the Result
