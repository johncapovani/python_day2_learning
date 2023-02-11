# Pure function as it will not be changing globally
# So the value is being updated internally within the function as if it was a global varaible but internally only. (That explanation may be confusing)
def count_down(n):
    # Base case
    if n == 0:
        return
    else:
        print(n)
        # Recurrsion
        return count_down(n-1)


n = 8
count_down(n)