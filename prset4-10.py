n=input()
k="dhoni"
l=[]
if len(k)==len(n):
	for i in n:
		if i in k and i not in l:
			l.append(i)
if len(k)==len(l):
	print("yes")
else:
	print("no")
