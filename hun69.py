s=input()
c1=s.count("@")
c2=s.count(".")
i=s.index("@")
s1=s[:i]
l=len(s)
i1=s.index(".")
s2=s[i1::]
s3=s[i+1:i1]
if c1==1 and c2==1 and l>=3 and s2==".com" and len(s3)=="gmail":
	print("YES")
else:
	print("NO")
