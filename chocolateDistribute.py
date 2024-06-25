def chocolateDistribute(array,n,m):
    if m==0 or n==0:
        return 0
    if m>n:
        return -1
    array.sort()
    mindiff=array[n-1]-array[0]
    for i in range(n-m+1):
        mindiff=min(mindiff,array[i+m-1]-array[i])
    return mindiff
    

print(chocolateDistribute([12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50],17,7))
    