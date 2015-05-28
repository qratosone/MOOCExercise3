from math import sqrt
sum=0
n=input()
for i in range(2,n):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0 :
            break
    else:
        sum=sum+i
print sum
