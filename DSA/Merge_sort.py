def merge_sort(array:list):
    array_left=[]
    array_right=[]
    length=len(array)
    if length<=1:
     return
    middle=length//2
    i=0
    j=0
    for i in range(0,length):
       if i<middle:
          array_left.append(array[i])
       else :
          array_right.append(array[i])
          j+=1
    print(array_left,"      ",array_right)
    merge_sort(array_left)  
    merge_sort(array_right)
    merge(array_left,array_right,array)

def merge(leftarray,rightarray,array):
    leftsize=len(array)//2
    rightsize=len(array)-leftsize
    i,l,r=0,0,0
    while(l<leftsize and r<rightsize):
       if leftarray[l]<rightarray[r]:
          array[i]=leftarray[l]
          l+=1
          i+=1
       else:
           array[i]=rightarray[r]
           r+=1
           i+=1

    while(l<leftsize):
       array[i]=leftarray[l]
       i+=1
       l+=1
    while(r<rightsize):
       array[i]=rightarray[r]
       i+=1
       r+=1
    print("MERGE-----")
    print(leftarray,"       ",rightarray)

import time

def main():
   array=[3,5,2,6,5,8,9,1,4]
   print(array)
   merge_sort(array)
   print(array)
st=time.perf_counter()
main()
et=time.perf_counter()
print(et-st)           
