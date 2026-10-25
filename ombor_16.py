ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

eng_kop = max(ombor, key=ombor.get)
eng_kam = min(ombor, key=ombor.get)
jami = sum(ombor.values())

print(f"Eng ko'p: {eng_kop} ({ombor[eng_kop]} ta)")
print(f"Eng kam: {eng_kam} ({ombor[eng_kam]} ta)")
print(f"Jami mahsulot: {jami} ta")