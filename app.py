# Function to print Fibonacci numbers up to n
def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # for a new line

# Set the limit for Fibonacci numbers
limit = int(input("Enter the limit for Fibonacci numbers: "))
print_fibonacci(limit)

