#Escape characters
s="name\tplace\npantech\tT-nagar"
print(s)

#Concatenation of 2 strings
s1="abc"
s2="def"
s=s1+s2
print(s)

#String Operations
print("abc"+str(23))

print(len("abcdef"))

s="abcdefghi"
print(s.find("def"))

s="abcdefghi"
print(s[1:5])

print(s[:5])

s="abcdefghi"
print(s[3:])

s="wait wait wait until u succeed"
print(s.replace("wait","try"))

print("aBVG".upper())

print("aBVG".lower())

#Conditionals
x=101
if(x==34):
    print("Its 34")
elif(x>=34):
    print("It can be ur no.")
else:
    print("Its definitely not ur no.")

a=str(input("Enter the input string"))
a=a.casefold()
b=reversed(a)
if(list(a)==list(b)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

def count_to_10():
    for i in range(1,11):
        print(i)
count_to_10()