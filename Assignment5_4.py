#4.Write a program which contains one function that accepts string and one position from user.
#Remove the character from that position.
#Input : “ABCDEFGHIJK” Position : 5
#Output : “ABCDEGHIJK”

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

input_string=input("enter string:")

 
print(remove_char(input_string, 5))