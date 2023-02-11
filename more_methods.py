# Using the unpacking operator: Allows you to create a tuple

def class_room(*students):
    return (students)


print(class_room("Jerry", "Carl", "Pat"))

# Using a default argument to avoid failure


def get_name(first, last=""):
    return (f"Hello there {first} {last}")


# Using kwargs which stands for key work arguments and has two **

def kwargs(**kwargs):
    # Tells python that it is a dictionary data set that we are working with
    for value_type, name in kwargs.items():
        print(value_type)


# Allows you to assign key value pairs and create a dictionary
print(kwargs(first="kent", middle="jerry", last="clark"))
