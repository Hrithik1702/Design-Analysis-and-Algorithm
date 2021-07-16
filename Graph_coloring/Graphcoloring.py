def Graphcoloring(k):
    c=0
    while True:
        if c==0:
            print("\n$ Graphcoloring(",k,")")
        nextvalue(k)
        if x[k]==0:
            return
        if k==n:
            print("--> Solution State:",end=" ")
            print(x[1:])
            print()
        else:
            Graphcoloring(k+1)
        c=1

def nextvalue(k):
    print(" # nextvalue(",k,")")
    print("Assigned colours :",x[1:])
    c=0
    while True:
        x[k]=(x[k]+1)%(m+1)
        if x[k]==0:
            print("\nNo more colors available")
            return
        a=0
        if c==0:
            print("Adjacent nodes to",k,": ",end="")
        for j in range(1,n+1):
            if adj[k][j]==1 and c==0: 
                print(j,end=" ")
        for j in range(1,n+1):
            if adj[k][j]==1:
                if x[k]==x[j]:
                    a=1
                    break
        if a!=1:
            print()
            print("Colour of ",k," :",x[k])
            return
        c=1
m=int(input("No. of Colours"))
n=int(input("No. of Nodes"))
adj=[]
x=[]
for i in range(n+1):
    temp=[]
    for j in range(n+1):
        temp.append(-1)
    adj.append(temp)
e = int(input("Enter the no. of edges"))
for i in range(e):
    l = list(map(int,input().split()))
    adj[l[0]][l[1]]=1
    adj[l[1]][l[0]]=1
for i in range(n+1):
    x.append(0)
Graphcoloring(1)
        
