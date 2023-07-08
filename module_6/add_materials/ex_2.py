with open("data_2.txt","w") as fh:
    fh.write('First line\t')
    fh.write('Second line\n')
    fh.writelines(['Third line\n', 'Fourth line\n'])

with open("data_2.txt", "r+") as fh:
    print(fh.read())
    print(fh.write("text")) # 4


with open("data_2_2.txt", "r+") as fh:
    print(fh.write("text")) # 4 курсор сначала на 0 и поэтому мы перезаписываем 1 строку
    print(fh.read()) # textt line	Second line Third line ...
