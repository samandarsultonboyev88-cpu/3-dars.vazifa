harorat = (18, 20, 17, 23, 25, 21, 19)

yuqori_haroratlar = []
for h in harorat:
  if h > 20:
    yuqori_haroratlar.append(h)

print("Haroratlar:", ", ".join(map(str, yuqori_haroratlar)))
print(f"Kunlar soni: {len(yuqori_haroratlar)}")