from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        list_wrap = [p for p in (*args, *kwargs.values())]
#        print('1 - ', list_wrap)
        p_p = [f'{func.__name__}({p}: {type(p)})' for p in list_wrap]
        print(*p_p, *func(*args, **kwargs), sep=", \n")
    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    input_list = [p for p in (*args, *kwargs.values()) if isinstance(p, int) or isinstance(p, float)]
    return [p ** 3 for p in input_list]

calc_cube(5, 6, 1.1, {'er': 13}, 'abc', rt='4', tt=3)
#print(calc_cube(5, 6, 1.1))