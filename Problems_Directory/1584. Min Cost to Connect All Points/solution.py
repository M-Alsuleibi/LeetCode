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
