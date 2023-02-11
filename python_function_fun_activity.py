# Prompt: arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for value in args:
      print(f"I just saw a {value} driving on the road!")


args = arb_args("car", "motorcycle", "four wheeler", "tractor", "chicken")

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.


def inner_func(int_1, int_2):

   def distinct_1(int_1):
      if int_1 % 2:
         return "Int_1 is a prime number"
      else:
        return "Int_2 is not a prime number"

    def distinct_2(int_2):
        return int_2 + 1

    
    
    
   