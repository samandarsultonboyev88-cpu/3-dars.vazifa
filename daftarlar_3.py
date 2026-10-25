qoldi = 12

while qoldi > 0:
  sotildi = int(input("Sotildi: "))
  qoldi -= sotildi
  if qoldi > 0:
    print(f"Qoldi: {qoldi}")
  else:
    print("Qoldi: 0")
    print("Ombor bo'sh")
    break