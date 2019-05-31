s1,s2=map(str,input().split())
d=abs(len(s1)-len(s2))
c=0
if len(s1)>len(s2):
	dif=len(s1)-d
	st=s1[:dif]
	for i in range(len(st)):
		if st[i]!=s2[i]:
			c=c+1
else:
	dif=len(s2)-d
	st=s2[:dif]
	for i in range(len(st)):
		if st[i]!=s1[i]:
			c=c+1
print(d+c)			
