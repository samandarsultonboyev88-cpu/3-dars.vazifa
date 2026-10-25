birinchi = {"Ali", "Madina", "Jasur", "Aziza"}
ikkinchi = {"Jasur", "Sardor", "Aziza", "Bekzod"}

faqat_birinchi = birinchi.difference(ikkinchi)
faqat_ikkinchi = ikkinchi.difference(birinchi)
ikkalasida = birinchi.intersection(ikkinchi)

print("Faqat birinchi:", ", ".join(faqat_birinchi))
print("Faqat ikkinchi:", ", ".join(faqat_ikkinchi))
print("Ikkalasida:", ", ".join(ikkalasida))