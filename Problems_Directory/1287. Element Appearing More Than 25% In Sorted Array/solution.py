class Solution:
    def binarySearch(self,arr,x, isFirstOccur):
            res = -1
            L, R = 0, len(arr) - 1
            while L <= R:
                mid = (L+R) // 2
                if arr[mid] > x:
                    R = mid - 1
                elif arr[mid] < x : 
                    L = mid + 1
                else:
                    res = mid
                    if isFirstOccur:
                        R = mid - 1 # retrun the first occurrence of x
                    else:    
                        L = mid + 1 # retrun the last occurrence of x
            
            return res

    def findSpecialInteger(self, arr: List[int]) -> int:
        for num in arr: 
            firstOccur = self.binarySearch(arr,num,True)
            lastOccur = self.binarySearch(arr,num,False)
            numFreq = lastOccur - firstOccur + 1 
            if numFreq / len(arr) > 0.25:
                return num
