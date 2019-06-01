s=input()
c=0
for i in range(0,len(s)):
	co=s.count(s[i])
	if co>=c:
		c=co
		si=s[i]
print(si)
