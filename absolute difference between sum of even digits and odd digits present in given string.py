#wap to absolute difference between sum of even digits and odd digits are present in given string.
s = input("Enter a string of digits: ")  # Take input from the user
es = 0                                   # Initialize the sum of even digits to zero
os = 0                                   # Initialize the sum of odd digits to zero

# Loop through each character in the input string
for i in s:
    if i.isdigit():                      # Check if the character is a digit
        k = int(i)                       # Convert the character to an integer
        if k % 2 == 0:                   # Check if the integer is even
            es += k                      # Add the even integer to the sum of even digits
        else:
            os += k                      # Add the odd integer to the sum of odd digits

# Print the absolute difference between the sums of even and odd digits
print(abs(es - os))

# Print labels for odd and even sums
print("odd")
print("even")



#Example:
1.If the input string s is "123456":
2.The sum of even digits es will be 2 + 4 + 6 = 12.
3.The sum of odd digits os will be 1 + 3 + 5 = 9.
4.The absolute difference between es and os will be |12 - 9| = 3.
5.It will print:
3
odd
even
