class Solution(object):
    def minimumTotal(self, triangle):
        
         def tree(array,i,j):
              if len(array)-1==i:
                  return array[i][j]
              leftsum=tree(array,i+1,j)
              rightsum=tree(array,i+1,j+1)
              
              return array[i][j]+min(leftsum,rightsum)
         return(tree(triangle,0,0))