N = int(input())
A=list(map(int,input().split()))
answer = 1

for i in range(N):
    answer = (answer * A[i])%(10**9 + 7)

print(answer)
