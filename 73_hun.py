s=input()
s1=input()
l=[]
if s==s1:
	print(s)
else:
	for i in range(0,len(s)):
		for j in range(i+1,len(s)):
			k=s1[i:j]
			if k in s:
				l.append(k)
	print(max(l, key=len))
