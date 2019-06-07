from itertools import permutations
n=input()
prem=[''.join(p) for p in permutations(n)]
l=list(set(prem))
for i in l:
	print(i)
