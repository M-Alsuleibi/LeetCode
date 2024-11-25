# [2352. Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Collect each columns in a separete grid.
- Compare the new grid that contains the colums with the rows of the original grid.
<!-- # Approach -->
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(N^2)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(N^2)$$
# Code
```python3 []
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid) # Square matrix
        colsGrid = [ [] for i in range(n)] # Initialize n length list of lists
        count = 0   
        # This loop to construct columns grid
        for i in range(n):
            for j in range(n):
                colsGrid[j].append(grid[i][j])
        # Loop to compre each row in grid
        # with every row in colsGrid(columns of original grid)
        for i in range(n):
            for j in range(n):
                if grid[i] == colsGrid[j]:
                    count += 1
        return count

```


