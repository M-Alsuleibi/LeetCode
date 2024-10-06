# [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/) `MEDIUM`

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
1. Populate all possible edges between every pair of vertices, representing points, with corresponding weights (Manhattan distances).
2. Use Prim's or Kruskal's algorithm to find the minimum spanning tree (MST) that connects all points with the least cost.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Construct an adjacency list for all points, where each point is a vertex, and the weight between points is the Manhattan distance.
2. Use a min-heap to select the smallest edge at each step and ensure efficient edge selection.
3. Initialize a visited set to keep track of the points already included in the MST.
4. Start from an arbitrary point (e.g., vertex 0) and expand the MST by adding the smallest edge that connects a new point.
5. Accumulate the total cost (mst) as the sum of edge weights in the MST.
6. Return the total MST cost once all points are connected.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n^2 + nlogn)$$: building adjList(n^2) and Prim's algorithm execution(ElogE).
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n^2)$$
# Code
```python3 []
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # T O(n^2 + nlogn), M O(n^2)
        # Build an adjacency list with all possible weighted edges (Manhattan distances) between points
        adj = { i : [] for i in range(len(points))} # same as defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2) # Manhattan distance between points i and j
                # (undirected graph)
                adj[i].append((j, weight))
                adj[j].append((i, weight))  
       
        # print(adj)        
        # Initialize the heap by choosing a single point (in this case 0) 
        # and pushing all its neighbors in format (weight, src, neighbor)
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, (weight, 0, neighbor))
        visit = set()
        # adding 0 p[oint to visit set
        visit.add(0)

        # mst to sum MST weights
        mst = 0
        # Prim's Algothim to build the MST
        while minHeap:
            weight, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)    
            mst += weight    

            for neighbor, weight in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (weight, node, neighbor))
        
        return mst
```
