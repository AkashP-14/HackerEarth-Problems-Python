L = int(input())
N = int(input())
while N != 0 :
    T = list(map(int, input().split()))
    W = T[0]
    H = T[1]
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif W>=L and H>=L:
        if W == H:
            print("ACCEPTED")
        else:
            print("CROP IT")
    N = N-1