import string
s=input()
l=list(string.ascii_lowercase)
l1=[]
for i in s:
	m=i.lower()
	if m in l and m not in l1:
		l1.append(m)
if len(l1)==len(l):
	print("yes")
else:
	print("no")
