class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Brute Force: using DFS -> Tc = O(n^2)
        # Optimized : Using Union-Find DS -> Tc = O(n), Sc = O(n)
        par = [i for i in range(len(edges) + 1) ]
        rankBySize = [1] * (len(edges) + 1)

        # n is a node
        def find (n):
            p = par[n]

            while p != par[p]:
                par[p] = par[par[p]] # set the grand parent -Path compression
                p = par[p]
            return p

        #return False if cant complete
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rankBySize[p1] > rankBySize[p2]:
                par[p2] = p1
                rankBySize[p1] += rankBySize[p2]
            else:
                par[p1] = p2
                rankBySize[p2] += rankBySize[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]       

