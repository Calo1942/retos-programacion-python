reemplazos = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ñ": "n",
}

text = "áeioú"


for char in text:
    if char in reemplazos.keys():
        char = reemplazos[char]
        print(char)
