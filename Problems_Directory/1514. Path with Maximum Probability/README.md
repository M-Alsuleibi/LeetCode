# [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/description/) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem about finding "path with the maximum probability" in a wieghted graph, which is analogous to finding the "shortest path" in graph. However, There is a variation instead of return the minimum(shortest) we want return the maximum(expand the most probable path first).

The problem can be solved using a greedy algorithm, similar to Dijkstra's shortest path algorithm

# Approach
<!-- Describe your approach to solving the problem. -->
1. Graph Representation:

- We are given a list of edges and their corresponding probabilities, so the first step is to represent the graph using an adjacency list. Each node will map to a list of its neighbors, where each neighbor is a tuple `(neighbor_node, probability_of_traversal)`.
2. Modified Dijkstra's Algorithm:

- We use a **priority queue (max-heap)** to always explore the most probable path first. Since Python’s `heapq` is a min-heap by default, we store negative probabilities to simulate a max-heap.
The heap is initialized with the `start_node` and a probability of `1` (since starting at the node itself has full certainty).
- As we process each node, if we reach the `end_node`, we return the current probability as this is the maximum possible.
- For each node, we update the probabilities for its neighbors. If a higher probability path is found to a neighbor, we push this new path into the heap for future exploration.
3. Early Exit:

- The algorithm stops and returns the probability once we reach the `end_node`, as we are guaranteed that this is the path with the highest probability.
4. Edge Cases:

- If there is no valid path from the `start_node` to the `end_node`, we return `0`.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(ElogV)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(E + V)$$ for storing the adjacency list and heap.

# Code
```python3 []
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        Shortest path algorithm(Dijkstra's):
        Approach:
        1. Set-up the graph as an adjacency list using both edges and succProb lists.
        2. Slight variation of the shortest pathe since here we want the Max probability. We use a maxHeap and
        multiply corresponding weights not arithmatic summation.

        """
        # Step 1: Build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))

        # Step 2: Initialize max-heap with the starting node, and start probability as 1
        maxProb = {}
        maxHeap = [(-1, start_node)] # We store the negative probability for max heap purposes

        # Step 3: Process the graph using a modified Dijkstra's algorithm (maximize probability)
        while maxHeap:
            w1, n1 = heapq.heappop(maxHeap)
            if n1 in maxProb:
                continue
            maxProb[n1] = -1 * w1    # Probability to reach start_node is 1
            # Early exit if we reach the end_node
            if n1 == end_node:
                return -1 * w1

            for n2, w2 in adj[n1]:
                if n2 not in maxProb:
                    heapq.heappush(maxHeap, (w1 * w2, n2))

        return 0
        
```
