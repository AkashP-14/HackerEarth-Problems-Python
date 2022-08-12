tag = input()[:9]
vowels = "AEIOUY"
c=0
for i in range (len(vowels)):
    if tag[2]==vowels[i]:
        c+=1

for i in range(len(tag)-1):
    if i!=2 and i!=6 and i+1!=2 and i+1!=6:
        if (int(tag[i])+int(tag[i+1]))%2 !=0:
            c+=1  

if c>0: 
    print('invalid')
else: 
    print('valid')