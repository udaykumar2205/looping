#wap to print how many special character are present in given string.
s = input("Enter a string: ")  # Take input from the user
c = 0                          # Initialize the count of non-alphanumeric characters to zero

# Loop through each character in the input string
for i in s:
    if not i.isalnum():        # Check if the character is not alphanumeric
        c += 1                 # Increment the count of non-alphanumeric characters

# Print the count of non-alphanumeric characters
print(c)


#Example:
1.If the input string s is "Hello! How are you?":
2.There are 5 non-alphanumeric characters: '!', ' ', ' ', '?', '?'.
3.It will print:

Number of non-alphanumeric characters: 5
