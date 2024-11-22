#wap to print delete the vowels in given string.
s=input()
v='aeiou'
result=''
for ch in s:
    if ch not in v:
       result+=ch
       
print(result)
