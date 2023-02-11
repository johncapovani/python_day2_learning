# Prompt: arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for value in args:
      print(f"I just saw a {value} driving on the road!")


args = arb_args("car", "motorcycle", "four wheeler", "tractor", "chicken")

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.


def inner_func(int_1, int_2):

    def distinct_1(int_1, int_2):
      return int_1 + int_2

    def distinct_2(int_1, int_2):
        return int_2 * int_1

    return distinct_1(int_1, int_2) + distinct_2(int_1, int_2)

print(inner_func(5,25))

# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, preference=None):
  if preference == None:
    print(f"Hi {name}, today you're eating mystery meat. Because you did not specify what you prefer! :(")
  else:
     print(f"Hi {name}, today you're eating {preference}")

lunch_lady("John")
    
# sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(int_1, int_2):
   sum = int_1 + int_2
   product = int_1 * int_2

   return f"The sum is {sum} and the product is {product}."
  
print(sum_n_product(5,25))
    
# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args("dog", "giraffe")

# arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*args):
   print(f"The mean of your submission is {sum(args)/len(args)}")


arb_mean(1,2,3,4,5)
