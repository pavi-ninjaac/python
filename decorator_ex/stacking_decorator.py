def add_four(func):
    def wrapper_func(*args, **kwargs):
        print("We're adding 4")
        result = func(*args, **kwargs)
        return result + 4

    return wrapper_func

def double(func):
    def wrapper_func(*args, **kwargs):
        print("We're doubling")
        result = func(*args, **kwargs)
        return result * 2

    return wrapper_func

@double
@add_four
def add(a, b):
    print(f"We're adding {a} and {b}")
    return a + b

print(add(1, 3))