# Ülesanne 14 alamülesanne 1
# Mopeedid
kuud = ["jaanuar","veebruar","märts","aprill"] #Ja nii edasi
fail = open("mopeedid.txt", encoding="UTF-8")
mopeedid = []
# Igal real ühe kuu jooksul registeeritud mopeedide arv
# append() meetod lubab järjendile elemente juurde lisada
for rida in fail:
    mopeedid.append(int(rida))

kuu = int(input("Mis kuul registeeritud mopeedide arvu sa soovid(1-12):"))
print(kuud[kuu-1] + " kuul registeeriti " + str(mopeedid[kuu-1]) + " mopeedi")

fail.close()
