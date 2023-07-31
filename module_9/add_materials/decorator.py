from time import time

Debug = True

def args_logger(func):
    def inner(*args):
        if Debug:
            print(f"I'am args logger. Args: {args}")
        result = func(*args)
        return result
    return inner

def result_logger(func):
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f"I'am result logger. Result: {result}")
        return result
    return inner

def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        stop = time()
        if Debug:
            print(f"I'am timer.Run time: {stop - start}")
        return result
    return inner

@timer
@args_logger
@result_logger
def calc(x,y):
    result = x + y
    return result

#logger = args_logger(calc)


if __name__=="__main__":
    # print(logger(7, 9)) # I'am args logger. Args: (7, 9) 16
    print(calc(5, 8)) # I'am args logger. Args: (5, 8) I'am result logger. Result: 13 I'am timer.Run time: 0.005998373031616211 13
