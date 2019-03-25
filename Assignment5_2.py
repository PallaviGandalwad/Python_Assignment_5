#2.Write a program which contains one function that accepts string from user and return number
#of words from that string.
#Input : “Marvellous Infosystems by Piyush Khairnar”
#Output : 5

string=raw_input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
print("====================================================================")
print("Using split()")

test_string = "Marvellous Infosystems by Piyush Khairnar"
print ("The original string is : " +  test_string) 

# using split() 
# to count words in string 
res = len(test_string.split()) 
  
# printing result 
print ("The number of words in string are : " +  str(res)) 
