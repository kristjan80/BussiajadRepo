# Avame sisendandmed.txt faili, kus on lihtsalt mingid numbrid
# Hea oleks, kui fail asub samas kohas kus meie rakenduse põhikoodi fail
# VÕI sellest allpool kuskil kataloogis

# 1. Asi -> Avame faili

sisendfail = open("sisendandmed.txt", encoding="UTF-8")
palkadeSumma = 0
for rida in sisendfail:
    print(rida.strip())
    palkadeSumma = palkadeSumma + float(rida)
# fail tuleb alati sulgeda!
sisendfail.close()
print("Palkade kogusumma failist on:" + str(palkadeSumma))