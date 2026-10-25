jami = 0
soni = 0

while True:
  xarajat = int(input())
  if xarajat == 0:
    break
  jami += xarajat
  soni += 1

print(f"Jami: {jami}")
print(f"Kiritilgan xarajatlar soni: {soni}")

if soni > 0:
  ortacha = jami / soni
  print(f"O'rtacha: {ortacha:.2f}")
else:
  print("O'rtacha: 0")
  