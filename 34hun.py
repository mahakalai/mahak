from itertools import permutations
perms = []
s=input()
for p in permutations(s):
	m=''.join(p)
	if int(m)>int(s):
		perms.append(int(m))
l=sorted(perms)
if len(l)==0:
	print("impossible")
else:
	print(l[0])
