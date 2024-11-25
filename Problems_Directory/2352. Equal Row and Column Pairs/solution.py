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
