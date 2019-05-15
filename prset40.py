#maha
s=input()
k="dhoni"
l=[]
if len(k)==len(s):
	for i in s:
		if i in k and i not in l:
			l.append(i)
if len(k)==len(l):
	print("yes")
else:
	print("no")
