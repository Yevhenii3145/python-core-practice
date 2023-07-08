task = """Разработайте функцию sanitize_file(source, output), переписывающую
в текстовый файл output содержимое текстового файла source, очищенное от цифр.
Требования:
-прочтите содержимое файла source, используя менеджер контекста with и режим "r".
-запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
-запись нового содержимого файла output должна быть единоразовая и использовать метод write
"""


def sanitize_file(source, output):
    data = []
    with open(source, "r") as fh:
        for line in fh:
            new_str = ""
            for char in line:
                if not char.isdigit():
                    new_str += char
            data.append(new_str)

    target_file = "".join(data)
    with open(output, "w") as fh:
        fh.write(target_file)


sanitize_file("task_7_source.txt", "task_7_output.txt")
