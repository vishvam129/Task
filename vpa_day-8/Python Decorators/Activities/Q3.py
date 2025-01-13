# Caching Results Decorator
def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
print(fibonacci(10))  

def to_uppercase(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@to_uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("world"))
