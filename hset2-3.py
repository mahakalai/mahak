s=input()
s1=list(s)
l1=[]
s2=""
for i in reversed(s1):
	l1.append(i)
s2=s2.join(l1)
if s==s2:
	print("YES")
else:
	print("NO")
