#wap how many vowels are present in given string.
s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i in s:
        c+=1
print(c)

#expalnation:
1.Take an input string from the user to store it in the variable in 's'.
2.define a string containing all the vowels(both lowercase to uppercase).
3.intializes the counter to zero,which will be used to count the number of vowels in the
string 's'.
4.iterates over each character in the string 's'.
5.check if the current character 'i' is one of the vowel in 'v'.
6.increment the counter 'c' if the condition is true(if the character is vowel).
7.print the total count of vowels after the loop has finished.


#Example
Let's consider an example where the input string s is "Hello, World!":

The string v contains the vowels: 'aeiouAEIOU'.
The loop iterates over each character in "Hello, World!":
H is not in v, so c remains 0
e is in v, so increment c (c = 1)
l is not in v, so c remains 1
l is not in v, so c remains 1
o is in v, so increment c (c = 2)
, is not in v, so c remains 2
(space) is not in v, so c remains 2
W is not in v, so c remains 2
o is in v, so increment c (c = 3)
r is not in v, so c remains 3
l is not in v, so c remains 3
d is not in v, so c remains 3
! is not in v, so c remains 3
The final count c will be 3 because there are three vowels in "Hello, World!".







