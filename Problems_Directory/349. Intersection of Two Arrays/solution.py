class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute force: Tc:O(n1 +n2) , Sc: O(n1 + n2)
        
        # Declare 2 sets for each array
        set1 = set()
        set2 = set()

        #iterate over each array

        for num1 in nums1:
            set1.add(num1)

        for num2 in nums2:
            set2.add(num2)

        # Retrive the intersect Set
        intersectSet = set1 & set2 # or set1.intersect(set2) 

        # Typecasting the set to List object to return
        return list((intersectSet))               
