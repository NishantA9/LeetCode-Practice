# If input is divisible by 3, print "Fizz"
# If input is divisible by 5, print "Buzz"
# If input is divisible by 3 and 5, print "FizzBuzz"
# Otherwise, print the input
#add try and except for invalid input

def fizzbuzz(input):
    
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    # elif input == 0:
    #     return "Invalid input"
    # elif input < 0:
    #     return "Invalid input"
    return input
    
# Test cases
print(fizzbuzz(15))  # "FizzBuzz"
print(fizzbuzz(3))   # "Fizz"
print(fizzbuzz(5))   # "Buzz"
print(fizzbuzz(7))   # 7

    
    
