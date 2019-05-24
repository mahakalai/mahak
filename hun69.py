s=input()
c1=s.count("@")
c2=s.count(".")
i=s.index("@")
s1=s[:i]
l=len(s)
i1=s.index(".")
s1=s[i1::]
if c1==1 and c2==1 and l>=3 and s1==".com":
	print("YES")
else:
	print("NO")
