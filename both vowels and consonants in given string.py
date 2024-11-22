#wap to check both vowels and consonants in given string.
s=input()
v='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
            print(f'vowels count is {vc}')
            print(f' consonants is {cc}')
