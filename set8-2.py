s=input()
l=list(s)
c=0
for i in range(0,len(l)):
	if l[i]=="a" or l[i]=="e" or l[i]=="i"  or l[i]=="o" or l[i]=="u":
		c=0
	else:
		c=c+1
if c==0:
	print("yes")
else:
	print("no")
