import time
st=time.time()

duplicate=[1,1,1,1,1,2,2,2,3,7,3,3,4,4,5,5,56,6,6,6]
unique=[]
for i in duplicate:
  
  while i not in unique:
    unique.append(i)
print(unique)
et=time.time()

print("net time {%.5f}",(et-st))
