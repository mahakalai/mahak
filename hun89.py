s=input()
l1=[]
s1=""
for i in range(0,len(s)):
	if s[i] not in l1:
		l1.append(s[i])
l1=l1[::-1]
s1=s1.join(l1)
print(s1)
