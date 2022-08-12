word = input()
zCount = 0
oCount = 0
for i in word:
    if i == 'z':
        zCount += 1
    elif i == 'o':
            oCount += 1
    else:
            pass
if zCount * 2 == oCount:
        print("Yes")
else:
        print("No")        
            