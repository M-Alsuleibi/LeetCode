class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        # Output: [[3,3],[-2,4]
        if k == len(points):
            return points

        distances = []
        minValuesArr = {} # ictionary to store lists of indices for each unique distance.
        
        for i in range(len(points)):
            sqrVal = (points[i][0]**2 + points[i][1]**2)**0.5
            distances.append(sqrVal)
            if sqrVal in minValuesArr:
                minValuesArr[sqrVal].append(i)
            else:
                minValuesArr[sqrVal] = [i]

        # To keep track of each sqrt value with its corresponding point, built a dict via dictionary comperhension
        # befor converting distances to minHeap
#        minValuesArr = { d:i for i,d in enumerate(distances)}
        heapq.heapify(distances) # Now distances becomes minHeap and lost its original list indexing

        resIdx = []
        while k: # Equivilent to wihle loop print(heapq.nsmallest(k, distances)) -> [sqrt(18),sqrt(20)]
            minVal = heapq.heappop(distances)
            indices = minValuesArr[minVal]
            # Iterate Indices: When popping distances from the heap, 
            # retrieve indices from the map and ensure you handle duplicates properly.
            while indices and k > 0:
                resIdx.append(indices.pop(0))
                k -= 1
                
        return [points[i] for i in resIdx]
        
