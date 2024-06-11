n=int(input("ENTER THE NO. OF ROWS WANTED"))
r=n
for i in range(n+1):
    for j in range(r):
          print(end=" ")
    if(i%2!=0):
     print("x"*(2*i-1))
    else:
     print("0"*(2*i-1))
    r-=1
 