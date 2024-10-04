class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_nod>
        """
        Shortest path algorithm(Dijkstra's):
        Approach:
        1. Set-up the graph as an adjacency list using both edges and succProb lists.
        2. Slight variation of the shortest pathe since here we want the Max probability. We >
        multiply corresponding weights not arithmatic summation.

        """
        # Step 1: Build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(n):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))

        # Step 2: Initialize max-heap with the starting node, and start probability as 1
        maxProb = {}
        maxHeap = [(-1, start_node)] # We store the negative probability for max heap purposes

        # Step 3: Process the graph using a modified Dijkstra's algorithm (maximize probabili>
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

