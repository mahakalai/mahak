import string
n=input()
k=input()
l=list(string.ascii_lowercase)
if len(n)==len(k):
    for i in range(0,len(n)):
        s=(l.index(n[i]))+(l.index(k[i]))
        if s>len(l):
            d=s-26
            print(l[d+1],end="")
        else:
            print(l[s+1],end="")
