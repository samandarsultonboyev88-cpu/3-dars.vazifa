boshlangich_pul = int(input("Boshlang'ich pul: "))
haftalik_qoshimcha = int(input("Haftalik qo'shimcha: "))

hafta = 0
jamgarma = boshlangich_pul

while jamgarma <= 500000:
  jamgarma += haftalik_qoshimcha
  hafta += 1

print(f"Kerakli hafta: {hafta}")