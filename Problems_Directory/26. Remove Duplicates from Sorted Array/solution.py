from typing import List #import it to resolve `NameError` when run removeDuplicates() in Driver code

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k        

# Driver code 
def main():
    input = [0,0,1,1,1,2,2,3,3,4]  
    solution = Solution()
    output = solution.removeDuplicates(input)
    print(output)
    print(input[:output])

if __name__ == "__main__":
    main()    