trans_map = {ord("Я"): "Ya", ord("н"): "n", ord("а"): "a", ord("о"): "o"}
ukr_name = 'Яна'
lat_name = ukr_name.translate(trans_map)
print(ukr_name, "=", lat_name, sep=' ')  # Яна = Yana

text = "Hello wоrld"  # специально написал русскую "о"
indx = text.find("world")
print(indx)  # -1
new_indx = text.translate(trans_map).find("world")
print(new_indx)  # 6
