class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        setting up the matrix boundries:
        L    R   
      T [1 2 3 ]
        [4 5 6 ] -> 1,2,3,6,9,8,7,4,5,6 -> In each cell I can move only in one direction
      B [7 8 9 ]
                    4 directions: left, down, right, up
        """
        T, L = 0, 0 
        B, R = len(matrix) -1 , len(matrix[0]) -1 
        # {"right":0,"down":1,"left":2,"up":3}
        direction = 0 
        result = []
        while T <= B and L <= R :
        # {"right":0,"down":1,"left":2,"up":3}
            if direction == 0 :
                for i in range(L, R + 1):
                    #print(matrix[T][i])
                    result.append(matrix[T][i])
                T +=1
            
            elif direction == 1 :
                for i in range(T, B + 1):
                    #print(matrix[i][R])
                    result.append(matrix[i][R])
                R -=1
                
            elif direction == 2 :
                for i in range(R, L - 1, -1):
                    #print(matrix[B][i])
                    result.append(matrix[B][i])
                B -=1

            elif direction == 3 :
                for i in range(B , T -1 , -1):
                    #print(matrix[i][L])
                    result.append(matrix[i][L])
                L +=1

            direction = (direction + 1) % 4

        return result    
