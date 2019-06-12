n=input()
n1=n[::-1]
c=0
if n==n1:
	print("yes")
else:
	s=n[::-1]
	for i in range(len(s)):
		if s[i]=="0":
			s1=s[i+1::]
			s2=s1[::-1]
			if s1==s2:
				c=c+1
			else:
				continue
		else:
			break
	if c>0:
		print("yes")
	else:
		print("no")
