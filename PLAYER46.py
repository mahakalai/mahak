import math
n=int(input())
if n==90:
	print("1")
else:
	r=math.radians(n)
	m=(round(math.sin(r),1))
	print(m)
