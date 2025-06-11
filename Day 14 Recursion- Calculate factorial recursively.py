def factorial(n):
    if n < 0:
        return "Factorial not defined for negatives"
    elif n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1)  # recursive step
        return result
# Example
print("Factorial Calculation")
number = int(input("Enter a number: "))
output = factorial(number)
print(f"Factorial of {number} is {output}")