def fibonacci(k):#used find fibonacci terms upto k
    i = 3
    fib = [0,1,1]
    nextterm = fib[i-1]+fib[i-2]
    while(nextterm<=k):
        fib.append(nextterm)
        i=i+1
        nextterm = fib[i-1]+fib[i-2]
    return fib
def findterms(k):#finds the optimal solution
    fib=fibonacci(k)
    ind=len(fib)-1#initialized to last index since iteration starts from end
    print("The fibonacci terms upto ",k," :",fib)
    count=0
    result=[]#stores the terms used for summation
    while(k>0):
        tempcount = k//fib[ind]
        count+=tempcount
        k=k%fib[ind];
        for i in range(1,tempcount+1):
            result.append(fib[ind])
        ind = ind -1
    print("count =",count)
    print("The terms=",result)

if __name__=='__main__':
    fib=[]
    k = int(input("Enter the value of k :"))
    findterms(k)

    
    
        
