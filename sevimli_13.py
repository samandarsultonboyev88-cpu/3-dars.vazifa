ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}

umumiy = ali.intersection(vali)
faqat_bittasiga = ali.symmetric_difference(vali)

print("Umumiy janrlar:", ", ".join(umumiy))
print("Faqat bittasiga yoqadi:", ", ".join(faqat_bittasiga))