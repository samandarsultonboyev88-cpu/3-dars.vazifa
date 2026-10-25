shaharlar = {"Toshkent": 3000000, "Farg'ona": 300000, "Samarqand": 600000}

kop_aholi = []
eng_kop_shahar = max(shaharlar, key=shaharlar.get)

for shahar, aholi in shaharlar.items():
  if aholi > 500000:
    kop_aholi.append(shahar)

print("500 000 dan ko'p:", ", ".join(kop_aholi))
print(f"Eng ko'p aholi: {eng_kop_shahar}")