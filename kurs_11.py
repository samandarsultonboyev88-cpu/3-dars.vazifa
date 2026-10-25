matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

ikkala_kursda = matematika.intersection(ingliz)
faqat_bitta = matematika.symmetric_difference(ingliz)

print("Ikkala kursda:", ", ".join(ikkala_kursda))
print("Faqat bitta kursda:", ", ".join(faqat_bitta))