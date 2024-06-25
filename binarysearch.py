def binarySearch(nums,beg,end,target):
        mid=beg+(end-beg)//2
        if end>=beg:
            if nums[mid]==target:
                  return mid
            if nums[mid]>target:
                return binarySearch(nums,beg,mid-1,target)
            else:
                 return binarySearch(nums,mid+1,end,target)
        else:
             return -1
            
print(binarySearch([1,4,4,4,4,6],0,5,4))