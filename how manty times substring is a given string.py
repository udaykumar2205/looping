#wap to check how many times given substring is present in the given string without using count method.
s=input()
sub=input()
c=0
for i in s:
    if i==sub:
        c+=1
print(c)


#explanation:
1.Take an input string from the user and stores it in the variable 's'.
2.Takes an input character(not substring)from the user and stores it in the variable 'sub'.
3.Intializes a counter 'c' to zero,which will be used to count the occurences of 'sub' in 's'.
4.iterates over each character in the string 's'.(for i in s:)
5.check if the current character 'i' is equal to 'sub'.(if i==sub)
6.increment the counter if the condition is true.(c+=1)
7.print the total number of occurences of 'sub' after the loop has finished.(print(c))
