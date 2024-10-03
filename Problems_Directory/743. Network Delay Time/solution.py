class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm.
        # T O(E logE), M O(E)

        # Phase 1: build the Adjacency List
        adjList = {}
        
        for i in range(1 , n + 1):
            adjList[i] = []

        for src, dst, w in times:
            adjList[src].append((dst, w))
    
        # Phase 2: Greedy Dijkstra's Algorithm core code
        minTimes = {}
        # Initialize the minHeap with the <cost, node> pair , takes the starting node(k) with ZERO cost
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in minTimes:
                continue
            minTimes[n1] = w1
            for n2, w2 in adjList[n1] :
                if n2 not in minTimes:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        # Phase 3: Calculate the maximum time taken to reach any node
        if len(minTimes) != n:
            return -1
        
        return max(minTimes.values())
           
