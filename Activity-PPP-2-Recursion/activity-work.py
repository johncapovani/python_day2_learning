#  Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def recursive(n):

    if n < 1:
        return print(f"Invalid submission value of {n}")
    # Base
    if n == 0:
        return
    else:
        print(n)
        recursive(n - 1)


n = -10
recursive(n)

# Write a function that prints the natural numbers from 1 to n. Below is a attempt that creates a recurssion error. I likely overcomplexed solution

# def natural_numbers(number):
    
#     def recursive_calculation(number):
#       start = 0
      
#       # Base
#       if start > number:
#         return list_output
#       else:
#         list_output =[]
#         value = recursive_calculation(start + 1)
#         list_output.append(value)

#     recursive_calculation(number)

# print(natural_numbers(5))

#2. Retry


# 3. Write a function that returns the nth elements in the Fibonacci Sequence.


# 4. Write a function that calculates the value of 'a' to the power of 'b'.
def power_up(base, expo):
   
  #  If the base is one its going to return itself
   if expo == 1:
      return base
  #  Recursion
   else:
      # Line 47 will keep calling the base function recalculating it with the new values until it stops
      return(base * power_up(base, expo - 1))
      
print(power_up(10,2))