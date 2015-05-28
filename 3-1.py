sum=0
n=input()
for i in range(0,n):
    if i%3==0 or i%5==0:
        sum=sum+i
print sum
