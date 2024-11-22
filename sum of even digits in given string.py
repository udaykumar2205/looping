#wap to sum of even digits present in given string.
s = input("Enter a string of digits: ")  # Take input from the user
sum = 0                                  # Initialize the sum of even digits to zero

# Loop through each character in the input string
for i in s:
    k = int(i)                         # Convert the character to an integer
    if k % 2 == 0:                     # Check if the integer is even
        sum += k                       # Add the even integer to the sum

# Print the sum of even digits
print(sum)


#Example:
1.If the input string s is "123456":
2.In the first iteration, i is '1'. After converting it to an integer,
k becomes 1, which is odd, so it is not added to the sum.
3.In the second iteration, i is '2'. After converting it to an integer,
k becomes 2, which is even, so it is added to the sum.
4.This process continues for each character in the string, and the final
sum of even digits is printed. For "123456", the sum of even digits will be 2 + 4 + 6 = 12.





