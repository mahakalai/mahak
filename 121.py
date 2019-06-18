s=input()
if s==s[::-1]:
	print(s)
else:
	for i in range(0,len(s)):
		s1=s[::i+1]
		s2=s[i+1::]
		if s1==s1[::-1] and len(s1)!=1:
			print(s1)
			break
		elif s2==s2[::-1] and len(s2)!=1:
			print(s2)
			break
		else:
			continue
