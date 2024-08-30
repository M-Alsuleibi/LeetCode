class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # cover [9,9,9] input array case will solve the problem
        # Tc = O(n) , Sc = (1)

        # Reverse the list instead of iterate from last 
        digits = digits[::-1]
        carry , i = 1 , 0
        
        while carry : 
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0 # Then i += 1  
                else:
                    digits[i] += 1
                    carry = 0 # this will terminate the loop


            else:
                digits.append(1)
                carry = 0 # this will terminate the loop   

            i += 1    

        return digits[::-1] # Reverse the result again     
