with open("logo.png", "rb") as fh:
    data = fh.read()
    print(data) # b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01h\x00\x00\x01h\x04\x03\x00\x00\x00\x88\xcb|\xe6\x00\x00\x00\x1bPLTE7v\xaa\xff\xcf>\xff\xd8H6o\x9f\xef\xef\xef\xff\xff\xff\x8c\xad\xc9\xf2\xe3\xa3\xc4\xd3\xe0\xd4\xc0\x00\xad\x00\x00 \x00IDATx\xda\xd4\\Mo\x1c7\x12%P\xb6\x90k\x13\x0e|n!A\xae\x05\xd0\x11|t6\x1a\xaf\x8eB0Rt\x14\xa0X\xf05\x80s7\xa0\xc8\xf0\xcf\xde&\xeb\x83\xc5\x9e\x9e\x19\xb2\xed\xe9\x99m;\xa3\xc8\x1d\xc4\xcf\xcf\x8fU\xaf\x8aE\xba\x1bz\xd6\x97\xf4|\xc3\xb7\xe9\xdf\xaf\xbe~y|<s\xfc\x9c\x9d=>>~\xfd\x1a_\xad\xbf\xdfot\xe9\xbe\xd3\xffku\xb3\x1e\xe0:\x87\x80.8} \x84\xe1\xa7s\x8f\x1f\xff=5\xd0\xab\x9b\xcb\x01pB7\xfd\x0c\xaf\x82{\xfc\xf7\xa4@_\r\x88\xdd\xbeg\x00~\xf6qu*\xa0\xaf\xee\xf7#\x16\xd8\xf8\xf1\xf2\xe6\x04@\xd7BN\xff\x15\x0e\xb0\x1f\t\xf6\x11A\xaf\xef\x87\x85W\xf9\xa0\xc0\xfe\xb8Z\x1f\x13\xf4\xfbZ\xc0L\xf4\xf0\t\x00\xe1\xecy}4\xd0\xeb\xcf\xae\xe5\x89\xb8\x01"\xf4\x80\x7f\xdd\x1c\t\xf4\xdd=6b\x8eL\x0f*\xc1\x81\xec\x8fG\x01\xbd\xba\xbbo@,\x7f\xbcA\x1c\x11\xfa\xa0\xec\x1f\x8e\x01\xba\ts\xe4\x19#^\xa4\x7f\x8d\\\xff\xb0<\xe8Fm\xb8\xcc4D\x81\xa0p\xbd$\xe8u+\xcf\x91\xdf\xb4\x0c\xa3\xb2\x93F \xfc\xb5,\xe8\xd5\xe7V\x8a\xe3\xdf\x0b&\x8a\x91\xa9\x1e\xb8\xfe0\x174\x7f]\xf1\xaf\xd7}{\xeb\x9a\x83\x1dE<\x127a\x1f"\xdfs\xe3\xef\xcb\xdf\xce\x02\xbd\x86f\xa2)\xad8\x12F\xd2G\xe4\xfa\xe2f1\xd0\xad\xe2\x00\x93\x13\x99i\xa0\'h\x9298\xe8[7\x83h\xe4\xc8\x81\xccrb\x1ap)\xa6W\xf7\xedk\x90\x96!\xa1\x17\x9a\x01s\x8e98\xe8YD\x8b\xa6I\x19\x12?\x06\x87\xfd\xbc\x08\xe8V\xa2Y\xd0\x00\xceYA\x0f\x88\xe3Gx\xbb\x08\xe8\xbb\xe6\x08\x8d\xc0\xfa@4\xa1\xa3\xa4\xfa\xb0\xa0\xdb\xf3\n\x13M\xc1:G\x8e\x18<\xe2?o\x96`\xda\xcd\x8a\xd1\xc2\xb4\xcb\xd1#$\x8d\x04\n \x87\x05}\xeb\xe6e\xc3\x18<\x12\xe1&v\x90\xaa_\x1e\x1e\xf4\xe7\xe6x\x87d\x95$J\xd3\xd7\x90P\'Q_\x1c\x1c\xf4f\xec8\xab\x03\x0eN3K!i\xa4\xa5xP\xd0\xe3\xd81T\xd6\xeb\xab]\xde:\xca"J\xd9\xa9\x9cI\x1b$\xe9\x98_\x92>\x0e\n\xba\x94\xf4\xd9s\n(\xeb\xad\xa8A\\)!.4\x9dP\x87d\x9bZA7\xfa\xe9w\x05\xa6g\xb6\xd7w\xb0\xcb*\xa5\x84H\xb1\x8e\xb5ArNl\x0fL\x87\xd5\x81\x8b\x80\'\x8b\xe9\x85\xbc]\xbd\xdfN5\xc9\x99%m\x14\x9dD\x1d\xa8\x1880\xe8\x02Q~\xbb~\xd8n\x95P\......'
    print(len(data)) #8478 байт

with open("new_logo.png", "wb") as file:
    file.write(data)
    print(type(data))
