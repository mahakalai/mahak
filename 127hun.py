n,k=list(map(str,input().split()))
l=[]
for i in n:
    for j in k:
        if i==j:
            l.append(i)
print("".join(l))
