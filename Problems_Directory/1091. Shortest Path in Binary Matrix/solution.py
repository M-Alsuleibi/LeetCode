class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        r = 0, c = 0
        queue = [(0,0), ]
        set =   {(0,0), }
        """
        # T O(V) , M O(V)
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        if not grid[0][0]: 
            queue.append((0,0))
            visit.add((0,0))

        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                # 8-directions differences:right,left,above,down,leftUpper,rightUpper,leftDown, rightDown   
                neighbors = [[0,1], [0,-1], [-1,0], [1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
                # row/column difference respectively
                for dr, dc in neighbors:
                    if ( min(r + dr, c + dc) < 0 or
                     max(r + dr, c + dc) == ROWS or
                       (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                            
            length += 1
            
        return -1    
