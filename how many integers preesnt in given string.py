#wap to sum of integers in given string.
s = input("Enter a string of digits: ")  # Take input from the user
sum = 0                                 # Initialize the sum of digits to zero

# Loop through each character in the input string
for i in s:
    k = int(i)                          # Convert the character to an integer
    sum += k                            # Add the integer to the sum

# Print the sum of digits
print(f'Sum of digits: {sum}')



#Example:
1.If the input string s is "12345":
2.In the first iteration, i is '1'. After converting it to an integer, k becomes 1,
and the sum becomes 1.
3.In the second iteration, i is '2'. After converting it to an integer, k becomes 2,
and the sum becomes 3 (1 + 2).
4.This process continues for each character in the string, and the final sum is printed.
For "12345", the sum of digits will be 15.
