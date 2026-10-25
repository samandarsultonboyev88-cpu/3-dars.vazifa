ovozlar = {
    "Ali": "Python",
    "Vali": "JavaScript",
    "Madina": "Python",
    "Jasur": "C++",
    "Aziza": "Python",
    "Sardor": "JavaScript",
}

tillar = {}
for ism, til in ovozlar.items():
  tillar[til] = tillar.get(til, 0) + 1

for til, son in tillar.items():
  print(f"{til}: {son} ta ovoz")

golib = max(tillar, key=tillar.get)
print(f"G'olib: {golib}")