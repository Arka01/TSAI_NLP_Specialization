1.
# write a python function to check user provided number is prime or not and print the result
def primeornot(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

primeornot(7)                

2.
# write a python program to swap two numbers and print it
num1 = 5
num2 = 10
temp = num1
num1 = num2
num2 = temp
print("The value of num1 after swapping: {}".format(num1))
print("The value of num2 after swapping: {}".format(num2))

3. 
# write a python function to add user provided list and return the result
def addlist(list1,list2):
    result = list1+list2
    return result

answer = addlist(['cat','dog'],['samsung','oneplus'])

4.
# write a python function to reverse user provided list and return the result
def reverselist(inlist):    
    inlist = inlist[::-1] 
    return inlist

result = reverselist([1,2])

5.
# write a python function to find the factorial of the user provided number and print the result
def findfactorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
        
findfactorial(3)        

6.
# write a python function to find the largest element in an array and return the result
def largest(arr):
    max = arr[0]
    n = len(arr)
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
        return max

largest([1,20,3])    

7.
# write a python function to check if a string is palindrome or not and print the result
def isPalindrome(s):
    if (s == s[::-1]):
        print("Given string is palindrome")
    else:
        print("Given string is not palindrome")

s = "malayalam"
isPalindrome(s)

8.
#Write a function to convert Kilometers to Miles
def Kilometers_to_Miles(km):
    conv_fac = 0.621371
    miles = km * conv_fac
    return miles

9. 
#Write a function to convert Miles to Kilometers
def Miles_to_Kilometers(m):
    conv_fac = 0.621371
    kilometers = m / conv_fac
    return kilometers    

10. 
#Write a function to Convert Celsius To Fahrenheit
def Celsius_To_Fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit

11.
#Write a fucntion to convert Fahrenheit to Celsius
def Fahrenheit_to_Celsius(f):
    celsius = (f - 32) / 1.8
    return celsius

12.
#Convert Decimal to Binary, Octal and Hexadecimal
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

13.
#Find ASCII Value of Character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


14.
#Multiply Two Matrices
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):

   for j in range(len(Y[0])):

       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

                
        



