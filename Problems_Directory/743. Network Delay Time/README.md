# [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires calculating the minimum time for signals to reach all nodes in a directed, weighted graph. My first thought was to use Dijkstra's algorithm, as it's effective for finding the shortest path in graphs with non-negative weights.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Build the graph: Represent the input as an adjacency list, where each node points to its neighbors with the respective travel times.
2. Apply Dijkstra's Algorithm: Use a min-heap (priority queue) to explore the shortest path from the source node `k`. The heap stores the current cost to reach each node, and for each node, we update its neighbors with the new cost if it's smaller.
3. Check reachability: After processing all nodes, check if all nodes were reached. If some nodes are unreachable, return `-1`.
4. Calculate result: The final result is the maximum time among all reachable nodes, which gives the time it takes for the signal to propagate to the farthest node.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(E logV)$$, _logV_ for each pop/push into the minHeap, multiplies by _E_ for all edges in worst case.
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(V+E)$$, for storing the adjacency list and the min-heap.
# Code
```python3 []
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
           
```
