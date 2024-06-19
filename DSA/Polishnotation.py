
def polish(exp):
    list1=[]
    list1=list(exp)
    list1.insert(0,'(')
    list1.append(')')
    nexp=[]
    stack=[]
    for i in range(0,len(list1)):
        print(i) 
        k=len(stack)
        if(list1[i]==')'):  # cHECKS FOR CLOSING BRACKETS
            print(' ) encountered')
            if len(stack)>0:
              while(stack[-1]!='('):
                print('-----------------------') 
            
                nexp.append(stack.pop())
                k-=1
                
                print(stack)
                print(nexp)       
                if len(stack)<=1:
                    break
              if stack[-1]=='(':
                  stack.pop()
        elif(list1[i].isalpha()==True)  :# CHECKS IF THE ELEMENT IS ALPHABET
            nexp.append(list1[i]) 
               
        elif len(stack)>0:

            if (stack[-1]=='*' or stack[-1]=='/') and (list1[i]=='+' or list1[i]=='-'):# CHECKS FOR PRECEDENCE

              print("here")

              nexp.append(stack.pop())
            stack.append(list1[i])  
        else :
             stack.append(list1[i])   
        print(list1) 
        print(stack)
        print(nexp)
       
       
        
    print(list1)
    print(stack)
    print(nexp)
    return(' '.join(nexp))

print(polish('(A*(B+((C+D)*(E+F))/G))*H'))

