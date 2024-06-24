def repeatedSubstringPattern( s):
        """
        :type s: str
        :rtype: bool
        """
        x=[s[0]]
        length=len(s)
        if s.count(s[0])==len(s):
            return True
    
        
        for i in range(1,len(s)//2):
            x.append(s[i])
            lenx=i+1
            print("hello")
            if (length/lenx)%2==0 or (length/lenx)%2==1:
             print("HERE!",length/lenx,"".join(x))

             if ("".join(x)*int(length/lenx))==s:
                print 
                return True
                
            print(x)
        return False

print(repeatedSubstringPattern("abcabcabc"))
             