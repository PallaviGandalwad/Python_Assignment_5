#5. Accept string from user and return average of ascii value of characters from that string.
#Input : “ABCDE”
#Output : 67 ((65+66+67+68+69)/5)


# Program to find the ASCII value of the given character

# Change this value for a different result
c = input("Enter String:->>")

# Uncomment to take character from user
#c = input("Enter a character: ")

print("The ASCII value of '" + c + "' is",ord(c))