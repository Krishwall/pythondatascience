sen=input("Enter a sentence  :")
s=""
def isVowel(i):
    if i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u' :
        return True
    else:
        return False
for i in sen:
    if  isVowel(i):
        continue
    else:
        s=s+i
print(s)
print()
c=0

t=[]    

