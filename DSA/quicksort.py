def quicksort(arr:list,low,high):
    if low<high:
       pidx=partition(arr,low,high)
      # print(arr)
       quicksort(arr,low,pidx-1)
       quicksort(arr,pidx+1,high)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<pivot :
            i+=1
             #swap
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    i+=1
    temp=arr[i]
    arr[i]=pivot   
    arr[high]=temp
    print(arr)
    return (i)

    
'''for i in (a):
        if i<pivot:
            leftpart.append(i)
        else :
            rightpart.append(i)    
        print(leftpart,"    ",rightpart)
    quicksort(leftpart)
    quicksort(rightpart'''
import time
st=time.perf_counter()
arr=[3,5,2,6,5,8,9,1,4]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)
et=time.perf_counter()
print(et-st)