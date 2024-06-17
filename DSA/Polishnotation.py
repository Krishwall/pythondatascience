
def polish(exp):
    list1=[]
    list1=list(exp)
    list1.insert(0,'(')
    list1.append(')')
    nexp=[]
    stack=[]
    for i in range(len(list1)):
        if(list1[i].isalpha()!=True)       :
            stack.append(list1[i])     
        elif(list1[i]==')'):
            for j in range(i,0,-1):
                print(i)
                if(list1[j]=='('):
                     nexp.append(stack.pop())
                     break    
                
                      
        else: 
            nexp.append(list1[i])
    print(list1)
    print(stack)
    print(nexp)


polish('A+(B*C-(D/E!F)*G)*H')


 