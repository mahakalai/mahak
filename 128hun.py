s=input()
if s==s[::-1]:
	print(s)
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		s1=s[i:j]
		if s1==s1[::-1] and len(s1)>1:
			print(s1)
