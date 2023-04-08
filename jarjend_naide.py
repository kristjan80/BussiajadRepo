palgad = [2000,2015,1400.15,"Veel Mingi palk"]
# Üks viis pöörduda konkreetse elemendi poole järjendis, on kasutada indekseid
# Arvutid alustavad loendamist alati nullist, ehk esimene element on kohal 0 ja viimane kohal
# ELEMENTIDE_ARV - 1
print(palgad[3])

# Väljastame, et inimeste palgad

# Kõigepealt while
palkadeArv = len(palgad)
i = 0

# print(palkadeArv)
# Loendame nullist alates. Loendame nii kaua kuniks i väärtus on VÄIKSEM kui palgad massiivis olev elementide arv
#while i < palkadeArv:
#    print("Inimese " + str(i+1) + ". Palk on: " + str(palgad[i]))
#    i = i + 1

# For lihtsustab andmekogumitega tööd
i = 1

#if 2000 in palgad:
#    print("Kellegi palk on 2000")

for palk in palgad:
    print("Inimese " + str(i) + ". Palk on: " + str(palk))
    i = i + 1

    

