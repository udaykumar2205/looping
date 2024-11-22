#wap to sum of even digits present in given string.
s=input()
sum=0
for i in s:
    k=int(i)
    if k%2==0:
        sum+=k
print(sum)
    
