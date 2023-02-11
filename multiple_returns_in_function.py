# Python Function Features
# Multiple returns in one function

def get_ages(sign_up_age, current_age):
  return(sign_up_age,current_age,11)

# This function returns a tuple
ages = get_ages(14,22)
print(type(ages))

# The benefits of tuples such as unpacking

# You can set multiple variables at once by seperating the declarations by a comma

# Automatically returns a value as python knows the index. Say the tuple is coming from a third party you can ensure all of the values are in the same order. We are assiging it to the ages tuple

age_one, age_two, int = ages

print(age_one)
print(age_two)
print(int)