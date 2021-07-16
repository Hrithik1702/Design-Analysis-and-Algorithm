mat=[]
def bgraph(mat,k,n,p):
    bcost=[-1,0,999999,999999,999999,999999,999999,999999,999999,999999,999999,999999,999999]
    d= [-1,-1]
    for j in range(2,n+1):
        for s in range(1,j):
            if(mat[s][j]!=999999):
                minr=s
                break
        mincost= 9999999
        for r in range(1,j):
            if mincost > mat[r][j] + bcost[r] and mat[r][j]!=999999:
                minr= r
                mincost = min([mat[minr][j] + bcost[r],mincost])
        bcost[j]=mincost
        d.append(minr)
        print("j = ",j,"bcost[",j,"] =","bcost[",minr,"] + c[",minr,",",j,"] =",bcost[minr],"+",mat[minr][j]," =",bcost[minr]+mat[minr][j])
        print("d[",j,"] =",d[-1])
    p[1]=1
    p[k]=n
    for i in range(k-1,1,-1):
        p[i]= d[p[i+1]]
    print(p)
            
n=12
k=5
p=[]
mat=[]
for i in range(k+1):
    p.append(-1)
for i in range(n+1):
    temp=[]
    for j in range(n+1):
        temp.append(999999)
    mat.append(temp)
e = int(input("Enter the no. of edges"))
for i in range(e):
    l = list(map(int,input().split()))
    mat[l[0]][l[1]]=l[2]
bgraph(mat,k,n,p)
       
