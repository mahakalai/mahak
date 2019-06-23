s=input()
s1=input()
i=s.index("|")
m=s[:i]
k=s[i+1:]
a=m+s1
b=k+s1
if len(m)==len(b):
	z=m+"|"+k+s1
	print(z)
elif len(k)==len(a):
	z=m+s1+"|"+k
	print(z)
else:
	print("Impossible")
