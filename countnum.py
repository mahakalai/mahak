s=input()
l=list(s)
c=0
for i in range(0,len(l)):
    if l[i].isnumeric():
        c=c+1
print(c)
