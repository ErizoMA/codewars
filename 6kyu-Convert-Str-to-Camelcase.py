text = "The_Stealth_Warrior"
if len(text) > 0:
    sameText = text.replace("-", "_")
    x = text.split("_")

    str = x[0]

    for i in x[1:]:
        str += i.capitalize()
else:
    str = ""

print(str)
