s=input()
s1=input()
s=s+s1
i=s.index("|")
if len(s[:i])==len(s[i+1:]):
	print(s)
else:
	print("Impossible")
