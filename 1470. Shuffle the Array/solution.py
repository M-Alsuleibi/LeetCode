class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffledArr = []
        L , R = 0 , n 

        for L in range(n):
            shuffledArr.append(nums[L])
            shuffledArr.append(nums[R])
            L += 1
            R += 1
        return shuffledArr
