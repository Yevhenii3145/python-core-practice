def formatted_numbers():
    list = []
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal","hex","binary")
    list.append(header)
    for i in range(16):
        new_str = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
        list.append(new_str)
    return list

a = formatted_numbers()
for el in a:
    print(el)
