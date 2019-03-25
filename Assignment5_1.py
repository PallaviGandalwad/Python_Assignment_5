#1.Write a program which contains one function that accepts string from user and return reverse
#of that string.
#Input : “Marvellous Pune”
#Output : “enuP suollevraM”

def Reverse(string):
	str=""
	for i in string:
		str =i+str
	return str


str=input("Enter String:")

print("input String :",end="")
print(str)

print("Reverse String:",end="")
print(Reverse(str))
