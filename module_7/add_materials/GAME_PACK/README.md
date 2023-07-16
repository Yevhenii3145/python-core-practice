Гайд: https://packaging.python.org/en/latest/tutorials/packaging-projects/

Для создания пакета создали виртуальное окружение в родительской папке содержащей setup.py и файлы пакета, в данном случае это папка GAME_PACK
обновили pip командой
# python.exe -m pip install --upgrade pip

Установили пакет build командой (WINDOWDS)
# py -m pip install --upgrade build

Чтобы забилдить пакет прописываем (WINDOWDS)
# py -m build

Чтобы можно было залить пакет на тестовый репозиторий устанавливаем библиотеку (WINDOWDS)
# py -m pip install --upgrade twine

Чтобы задеплоить пакет в репо нужно предварительно создать аккаунт на https://test.pypi.org/account/login/ , и прописываем в терминале
# py -m twine upload --repository testpypi dist/*
