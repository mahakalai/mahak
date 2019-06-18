s=input()
s2=s.lower()
l=[]
if s2==s2[::-1]:
	l.append(s2)
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		s1=s2[i:j]
		if s1==s1[::-1] and len(s1)>1:
			l.append(s1)
l1=sorted(l)
for i in l1:
	print(i)
