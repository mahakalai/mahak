import string
l=list(string.ascii_lowercase)
l.insert(0," ")
n,k=map(str,input().split())
s=0
if len(n)<len(k):
    l1=k[:len(n)]
    l2=k[len(n):]
    for i in range(0,len(n)):
        d=abs(l.index(n[i])-l.index(l1[i]))
        s=s+d
    su=s    
    for i in l2:
        su=s+l.index(i)
        
else:
    l1=n[:len(k)]
    l2=n[len(k)]
    for i in range(0,len(n)):
        d=abs(l.index(n[i])-l.index(l1[i]))
        s=s+d
    su=s    
    for i in l2:
        su=s+l.index(i)
print(su)        
