reemplazos = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    ",": "",
    " ": "",
    ".": "",
}

text = "ÁNA"
text = text.lower()

for i in reemplazos:
    if i in text:
        text = text.replace(i, reemplazos[i])

print(text)

xd = "hola"
print(xd[::-1])
