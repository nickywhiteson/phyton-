number = int(input("Enter a Number : "))

condition = (number%2 != 0) and (number%3 != 0 ) and (number%5 != 0) and (number%7 !=0)

if condition == True:
    print("This is a Prime Number")
else:
    print("This is not a prime number")