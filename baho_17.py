baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

yuqori_ballar = []
jami_ball = sum(baholar.values())
soni = len(baholar)

for ism, ball in baholar.items():
  if ball >= 90:
    yuqori_ballar.append(f"{ism} – {ball}")

print("Yuqori ball olganlar:", ", ".join(yuqori_ballar))
print(f"O'rtacha ball: {jami_ball / soni}")