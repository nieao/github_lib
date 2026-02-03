# Simple calculator for testing Claude Code Action

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # TODO: Add error handling for division by zero
    return a / b

if __name__ == "__main__":
    print(add(1, 2))
    print(divide(10, 0))  # This will cause an error
