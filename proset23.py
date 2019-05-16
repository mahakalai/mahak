#mahaa
n=input()
l=["GLGLGL","GRGRGR","GLLG","GRRG"]
c=0
for i in range(0,len(l)):
	if l[i] in n:
		c=c+1
if c==0:
	print("no")
else:
	print("yes")
		
