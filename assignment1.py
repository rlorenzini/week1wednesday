#ASSIGNMENT 1
#write app asks user for input and then prints factorial (X!, 4! is 4x3x2x1=24)
n = int(input("ENTER WHOLE NUMBER: "))

num = 1
while n>1:
    num = num * n
    n = n -1


print(num)



#ASSIGNMENT 2
#palindromes are strings which are same left to right as right to left (TACOCAT, RACECAR)
#create app that detects palindromes; ignore case sensitivity (assume all lowercase)
x = input("ENTER WORD: ")

def reverse(x):
    return x[::-1]

def isPalindrome(x):
    rev = reverse(x)
    if (x == rev):
        return True
    return False

ans = isPalindrome(x)

if ans == 1:
    print("PALINDROME")
else:
    print("NOT PALINDROME")




#ASSIGNMENT 3
#take input, find if number is prime or not (divisible by 1 and itself)

num = int(input("ENTER PRIME NUMBER: "))

i = num -1
prime = True

while i > 1:
    if num % i == 0:
        prime = False
    i = i-1

if prime == True:
    print("PRIME NUMBER")
else:
    print("NOT PRIME NUMBER")



#
