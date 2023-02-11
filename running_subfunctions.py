# Python Function Features

# Below is a example of calling a function that defines a new function then calls that new function to return a new value

def inner_funcs(int_param):
    
    def minus_five(inner_param):
        return(inner_param)
   
    new_value = minus_five(int_param)
    return(new_value)

# Use case example

# On click of warning don't show me this message again the onclick event triggers the action. Similar to a Factory Function

# Setting default values for variables in a function if there is a expected null value by setting the argument to a value as a default.

# Use case example: We are adding a new customer to a data base and need to do some logic on inputs. The user may have not populated a optional field. So to prevent the flow from breaking we can set the value to a default to prevent failure

# None is pythons equivelent to null. However you cannot use none for addition

def addition(num_one, num_two, num_three = 0):
    
    return num_one + num_two + num_three

print(addition(4,6))