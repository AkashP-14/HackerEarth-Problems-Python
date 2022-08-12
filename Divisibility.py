N= int(input())
arr=list(map(int,input().split()))
lastItem = arr[N-1]%10 
if lastItem == 0:
    print("Yes")
else:
    print("No")