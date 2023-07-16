Для создания нового виртуального окружения
в терминале заходим  в нужную папку и прописываем команду
# python -m venv my_env
или
# virtualenv my_env

В нашей таргетной папке появится папка виртуального окружения с названием my_env

Чтобы узнать с каким пайтоном мы работаем, тоесть с каким виртуальным окружением пропишем:
# which python
и получим папку, откуда мы берем пайтон например:
# /c/Users/Admin/AppData/Local/Programs/Python/Python311/python

для Windows, чтобы перейти из глобального пайтона в созданное вирт.окружение пишем:
# source my_env/Scripts/activate

Чтобы узнать список установленных пакетв в виртуальном окружении пишем:
# pip list
получим : # pip  23.1.2    setuptools  65.5.0

Команда which python теперь даст
# \Users\Admin\Desktop\python-core-practice\module_7\add_materials\my_env/Scripts/python

Чтобы выйти из виртуального окружения нужно ввести команду:
# deactivate

Чтобы получить установленные пакеты в виде списка прописываем:
# pip freeze

Чтобы записать список зависимостей в файл пишем:
# pip freeze > requirements.txt

Чтобы установить все зависимости из списка requirements.txt пишем:
# pip install -r requirements.txt

Чтобы установить самую последнюю версию какого-то пакета, или обновить версию уже установленного пакета пишем:
# pip install --upgrade sqlparse
или
# pip install --upgrade Django

Чтобы удалить пакет из виртуального окружения пишем:
# pip uninstall Django

Чтобы установить конкретную версию  например пакета Django пишем:
# pip install Django==4.0
