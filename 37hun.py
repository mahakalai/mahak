s=input()
c=0
for i in range(0,len(s)):
	s1=s[i+1::]
	s2=s1[::-1]
	if s[::i+1]==s2:
		c=1
		break
if c==1:
	print("YES")
else:
	print("NO")
