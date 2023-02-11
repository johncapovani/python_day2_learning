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

# COPIED BELOW FROM SOLUTION

def recursive_deduplicate(my_str, i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:], i)
    else:
      # no duplicate at current position, check next
      return recursive_deduplicate(my_str, i+1)


print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))

# 6. recursive_reverse — Uses recursion to reverse a string.


def recursive_reverse(str, i=0):
  # empty string case
  if len(str) == 0:
    return ""
  # base case
  elif i == len(str)-1:
    return str[0]
  else:
    # recursive case
    return str[-1-i] + recursive_reverse(str, i+1)
