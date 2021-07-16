n=int(input("enter no of items"))
c=int(input("enter capacity"))
w=list(map(int,input().split()))
w.insert(0,0)
v=list(map(int,input().split()))
v.insert(0,0)
f=[[0]*(c+1)]
for i in range(n+1):
    l=[0]
    for j in range(1,c+1):
        l.append(-1)
    f.append(l)
    
for i in range(1,n+1):
    print("i=",i," v",i,"=",v[i]," w",i," =",w[i])
    for j in range(1,c+1):
        print("F[",i,j,"] =>",end=" ")
        print("j-w[i]=",j-w[i],end=" ")
        if j-w[i]<0:
            print("<0","∴F[",i,",",j,"] = F[",i-1,",",j,"]  = ",f[i-1][j])
            f[i][j]=f[i-1][j]
        else:
            f[i][j]=max([f[i-1][j],v[i]+f[i-1][j-w[i]]])
            print(">=0","∴F[",i,",",j,"] = max(F[",i-1,",",j,"],",v[i],"+","F[",i-1,",",j-w[i],"] ) = ","max(",f[i-1][j],",",v[i]+f[i-1][j-w[i]],") =",f[i][j])
        print()
    print(f[i])
    
