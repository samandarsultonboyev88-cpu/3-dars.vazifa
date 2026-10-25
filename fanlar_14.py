ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}

ruxsat_etilgan = tanlangan.intersection(ruxsat)
ruxsat_etilmagan = tanlangan.difference(ruxsat)

print("Ruxsat etilgan:", ", ".join(ruxsat_etilgan))
print("Ruxsat etilmagan:", ", ".join(ruxsat_etilmagan))