# Args in python
# Using *args will handle any value that is submitted
# * is a unpacking operator that seperates everything apart
def addition(*args):
    print(type(args))
    return sum(args)

print(addition(10,5))