from functools import wraps


def val_checker(y):
    def _checker(func):
        @wraps(func)
        def wrapper(args):
            if y(args):
                print(func(args))
            else:
                raise ValueError('Wrong input', {args})

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    calc_cube(2)
    calc_cube(-2)

except (ValueError, NameError, TypeError) as err:
    print(err)
