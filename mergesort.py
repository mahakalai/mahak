def merge(a,b):
   l=[]
   while len(a)!=0 and len(b)!=0:
        if a[i]<a[j]:
           l.append(a[i])
           c=a=[0]
           a.remove(c)
        else:
           l.append(b[j])
           c=b[0]
           b.remove(c)
   if len(a)==0:
     l=l+a
     
   else:
     l=l+b
   return(l)
def sort(x):
   a=[]
   b=[]
   if len(x)!=0 or len(x)!=1:
        mid=len(x)//2
        a=sort[:mid]
        b=sort[mid:]
        merge(a,b)
   else:
        return(x)
 x=[int(k) for k in input().split()]
 res=sort(x)
 print(res)
        
        
  
