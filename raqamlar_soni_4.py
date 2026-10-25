son = int(input())
raqamlar_soni = 0

if son == 0:
  raqamlar_soni = 1
else:
  while son > 0:
    raqamlar_soni += 1
    son = son // 10

print(f"Raqamlar soni: {raqamlar_soni}")
