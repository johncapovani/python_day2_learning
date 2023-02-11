# 1. name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key} Value: {value}")


name_args(firstName="Jack", lastName="Sparrow")

# 2. all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.


def all_true(input):
    return all(input)


input = ([True, False])

print(all_true(input))

# 3. one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.


def one_true(numbers):
    return any(numbers)

print(one_true([True,False,False]))

# 4. recursive_factorial - Uses recursion to find the factorial of an integer.

def recursive_factorial(int):
    
    if int <= 1:
        return 1
    else: 
        return (int * recursive_factorial(int - 1))

print(recursive_factorial(5))