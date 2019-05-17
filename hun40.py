n=int(input())
s1=str(n)
l=list(s1)
s=0
for i in l:
    s=s+int(i)
s1=str(s)
l1=list(s1)
l2=l1[::-1]
if l1==l2:
    print("YES")
else:
    print("NO")
