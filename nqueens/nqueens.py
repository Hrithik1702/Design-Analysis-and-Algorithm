#1 - Based indexing
def place(k,i):
    for j in range(1,k):
        if(x[j]==i or abs(x[j]-i) == abs(k-j)):
            return False
    return True

def NQueens(k,n):
    for i in range(1,n+1):
        if place(k,i):
            x[k]=i
            if(k==n):
                print("Solution:",x)
            else:
                NQueens(k+1,n)

n=int(input("Enter the no. of queens"))
x=[]
for i in range(n+1):
    x.append(-1)
NQueens(1,n)
    
