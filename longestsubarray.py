def longestSubarray( nums, limit: int) -> int:
        subarray=[]
       
        
        diff=0
        longlength=0
        length=len(nums)
        for i in range(length):
            
            for j in range(i,length):
                maxi=0
                mini=1000000000
                subarray.append(nums[j])
                for k in range(len(subarray)):
                    maxi=max(maxi,subarray[k])
                    mini=min(mini,subarray[k])
                print(maxi,mini) 
                if (limit>=(maxi-mini) and (maxi-mini)>=diff):
                    print("HERE")
                    
                    
                    print("hello?")
                    diff=maxi-mini
                    print(len(subarray))
                    if len(subarray)>longlength:
                         longlength=len(subarray)
                         print(longlength)
                         print(subarray)
                         
                         print(maxi,mini)
                
            subarray.clear()
            
        return longlength
print(longestSubarray([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39],87))
