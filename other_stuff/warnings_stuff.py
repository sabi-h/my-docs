import warnings


def new_function(a: int, b=2):
    return a + b + 2


def old_function(a: int, b=2):
    warnings.warn("Use new_function", DeprecationWarning)
    print("yaay")
    return a + b + 1


print(old_function(1, 2))
