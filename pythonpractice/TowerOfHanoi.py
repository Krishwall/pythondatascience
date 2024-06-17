import time
st=time.perf_counter()
def towerHanoi(n,fromrod,torod,extrarod):
   if n==0:
        return 
   
   towerHanoi(n-1,fromrod,extrarod,torod)
   
   print("move disk",n,"from",fromrod,"to",torod)
   
   towerHanoi(n-1,extrarod,torod,fromrod)

n=4
towerHanoi(4,"A","B","C")
et=time.perf_counter()
print(et-st)