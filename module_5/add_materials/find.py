files = ["video.avi", "audio.mp3", "document.doc", "folder", "backup.tar.gz"]
for file in files:
    # index = file.rfind(".")
    # if index != -1:
    #     suffix = file[index+1:]
    #     print(f"File: {file} Index: {index} Suffix: {suffix}")
    # else:
    #     print(f"File: {file} Suffix: not found")

    try:
        index = file.rindex(".")
        suffix = file[index+1:]
        print(f"File: {file} Index: {index} Suffix: {suffix}")
    except:
        print(f"File: {file} Suffix: not found")
