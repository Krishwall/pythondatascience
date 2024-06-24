def dailyTemperatures( temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        stack=[]
        for i,j in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<j :
                  ptr=stack.pop()
                  answer[ptr]=i-ptr
            stack.append(i)      
            print(stack)
            print(answer)
dailyTemperatures([73,74,75,71,69,72,76,73])