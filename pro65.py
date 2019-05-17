n,k= map(int,input().split())
l= list(map(int,input().split()))
amount= int(input())
refund= (sum(l)-l[k])//2
if amount == refund:
  print("Bon Appetit")
else:
  print(amount-refund)
