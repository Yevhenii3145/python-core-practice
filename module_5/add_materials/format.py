numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
header = "|{:^15}|{:^15}|{:^15}|".format("int", "int^2", "int^3")
separator = "-"*len(header)
body = ""
for num in numbers:
    body += "|{:^15}|{:^15}|{:^15}|\n".format(num, num**2, num**3)
table = "\n".join([separator, header, separator, body, separator])
print(table)
# print(separator, header, separator, body, separator, sep="\n")

header_2 = "|{:^15}|{:^15}|{:^15}|{:^15}|".format("int", "dex", "oct", "bin")
separator_2 = '_'*len(header_2)
body_2 = ""
for num in numbers:
    body_2 += "|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n".format(num)
table_2 = '\n'.join([separator_2, header_2, separator_2, body_2, separator_2])
print(table_2)
