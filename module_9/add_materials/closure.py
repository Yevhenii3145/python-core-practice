def outer(x):
    def inner(y):
        print(f"{x} + {y} = {x + y}")
    return inner


def get_cache(cache=None):
    if cache is None:
        cache = {}

    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum([i for i in range(1, n+1)])
            print(f"Hard work {n} | ")
            return cache[n]
        else:
            print(f"Easy work {n} |")
            return cache[n]
    return inner


def main():
    adder_two = outer(2)
    adder_two(8) # 2 + 8 = 10
    adder_three = outer(3)
    adder_three(8) # 3 + 8 = 11


    data = {5: 15, 10: 55, 15: 120}
    calc = get_cache()
    print(calc(5))  # {} Hard work 5 |  15
    print(calc(5))  # {5: 15} Easy work 5 |  15
    print(calc(10))  # {5: 15} Hard work 10 | 55
    print(calc(10))  # {5: 15, 10: 55} Easy work 10 | 55
    print(calc(15))  # {5: 15, 10: 55} Hard work 15 | 120
    print(calc(5))  # {5: 15, 10: 55, 15: 120} Easy work 5 | 15

    calc_2 = get_cache(data)
    print(calc_2(10)) # {5: 15, 10: 55, 15: 120} Easy work 10 | 55
    print(calc_2(15)) # {5: 15, 10: 55, 15: 120} Easy work 15 | 120
    print(calc_2(5)) # {5: 15, 10: 55, 15: 120} Easy work 5 | 15




if __name__ == "__main__":
    main()
