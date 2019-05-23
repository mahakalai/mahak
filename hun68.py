n=int(input())
l=[int(x) for x in input().split()]
m=max(l)
mi=min(l)
print(l.index(mi)+1,l.index(m)+1)
