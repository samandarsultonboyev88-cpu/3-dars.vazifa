A = (3, 7)
B = (8, 2)

yigindi_A = sum(A)
yigindi_B = sum(B)

print(f"A yig'indisi: {yigindi_A}")
print(f"B yig'indisi: {yigindi_B}")

if yigindi_A > yigindi_B:
  print("A yig'indisi katta")
elif yigindi_B > yigindi_A:
  print("B yig'indisi katta")
else:
  print("Yig'indilar teng")
  