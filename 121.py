s = input()
n= 0
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    s1= s[i:j+1]
    if s1 == s1[::-1]:
      if len(s1) > n:
        n = len(s1)
        c = s1
print(c)
