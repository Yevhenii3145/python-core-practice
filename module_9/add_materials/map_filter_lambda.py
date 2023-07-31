import math

def get_length(d):
    result = d * math.pi
    return result

get_length_lambda = lambda d: d * math.pi

def get_ost(data):
    result = []
    for n in data:
        ost = n % 2
        result.append(ost)
    return result

def check_num(data):
    result = []
    for n in data:
        ost = n % 2
        if ost:
            result.append(n)
    return result

if __name__=="__main__":
    length_1 = get_length(10)
    length_2 = get_length_lambda(10)
    print(length_1, length_2, sep=" | ") # 31.41592653589793 | 31.41592653589793

    data = [1,2,3,4,5,6]

    ost_1 = get_ost(data)
    print(*ost_1) # 1 0 1 0 1 0
    print(*map(lambda n : n % 2, data)) # 1 0 1 0 1 0

    check_data = check_num(data)
    print(*check_data) # 1 3 5

    check_data_filter = filter(lambda x: x % 2, data)
    print(*check_data_filter) # 1 3 5
