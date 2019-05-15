n=input()
for i in range(1,len(n)):
	if n[0]<n[i]:
		print(n[i:])
    break
	
