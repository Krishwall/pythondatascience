def search(nums, target: int) -> int:
        k=-1

        if target==nums[-1]:
            return len(nums)-1
        elif target==nums[0]:
            return 0
        
        

        while True:
            if nums[k]>=nums[k+1]:
               
               break
            k+=1
        if target==nums[k]:
            return k
        
        
        if target<=nums[k] and nums[0]<=target  :
            for i in range(0,k):
                if target==nums[i]:
                    return i
            
    
        if target>=nums[k+1] and nums[-1]>=target  :
            for i in range(k,len(nums)):
                if target==nums[i]:
                    return i
        return -1    
print(search([3,5,1],5))