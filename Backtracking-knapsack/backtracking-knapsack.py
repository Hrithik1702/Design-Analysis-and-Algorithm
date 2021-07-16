def bound(cp,cw,k):
    b=cp
    c=cw
    for i in range(k+1,n+1):
        c=c+w[i]
        if c < m:
            b=b+p[i]
        else:
            return b+(1-(c-m)//w[i])*p[i]
    return (b)
def knapsack(k,cp,cw):
    print("----> Bknap(",k,",",cp,",",cw,")")
    print("k=",k,"cw =",cw,"w[k] =",w[k],"m =",m)
    if cw+w[k]<=m:
        y[k]=1
        print("\ny=",y[1:])
        if k<n:
            knapsack(k+1,cp+p[k],cw+w[k])
        if (cp+p[k]>fp[0]) and k==n:
            print("cp+p[k] = ",cp,"+",p[k]," > fp =",fp[0]," k==",n)
            fp[0]=cp+p[k]
            fw[0]=cw+w[k]
            print("fp = cp+p[k] = ",cp,"+",p[k],"= ",fp[0])
            print("fw = cw+w[k] = ",cw,"+",w[k],"= ",fw[0])
            for j in range(1,k+1):
                x[j]=y[j]
            print("x=",x[1:]) 
    print("fp=",fp[0],"<=","bound(",cp,",",cw,",",k,") =",bound(cp,cw,k),end=" ")
    if fp[0]<=bound(cp,cw,k):
        print("True")
        y[k]=0
        print("y=",y[1:])
        if k<n:  
            knapsack(k+1,cp,cw)
        if cp>fp[0] and k==n:
            print("fp = cp = ",cp)
            print("fw = cw = ",cw)
            fp[0]=cp
            fw[0]=cw
            for j in range(1,k+1):
                x[j]=y[j]
            print("x=",x[1:])
    else:
            print("False")
   
cp=0
cw=0
fp=[-1]
fw=[-1]
w=[]
p=[]
x=[]
y=[]
n=int(input("Number of items: "))
w=list(map(int,input().split()))
p=list(map(int,input().split()))
w.insert(0,0)
p.insert(0,0)
for i in range(0,n+1):
    x.append(-1)
    y.append(-1)
m=int(input("Max Knapsack Weight Capacity: "))
knapsack(1,cp,cw)
print(x[1:])

