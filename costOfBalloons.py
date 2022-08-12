T = int(input())

for i in range(T):

   costG, costP = map(int, input().split())

   n = int(input())

   a = 0
   b = 0

   for k in range(n):
        status = list(map(int,input().split()))
        a = a + status[0]
        b = b + status[1]

   print(min((a*costG+b*costP),(a*costP+b*costG)))