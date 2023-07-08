import shutil
import os
shutil.make_archive("new_archive", "zip","images")
shutil.unpack_archive("new_archive.zip","images/unpacked")
#os.rmdir("images/unpacked") # OSError: [WinError 145] Папка не пуста: 'images/unpacked'
shutil.rmtree("images/unpacked")
shutil.copy("data.txt", "images/new_archive")
