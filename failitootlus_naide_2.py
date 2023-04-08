# Failidega töötamine kus real on MITMEID andmesissekandeid
# Loome rakenduse, mis väljastab nime, palgad ja kogupalga
palkadeSumma = 0

sisendfail = open("sisendandmed_2.txt", encoding="UTF-8")

# Alustame standartse for tsükliga, et rida rea haaval
# andmekogum ehk fail läbi käia
for rida in sisendfail:
    # Meetodeid annab kombineerida!
    # Split tükeldab sõne vastavalt etteantud sümbolite jadale
    # print(rida.strip().split(" "))
    # Ka nii oleks võimalik jätkata
    #for andmetykk in rida.strip().split(" "):
    #    print(andmetykk)
    reaJarjend = rida.strip().split(" ")
    taisnimi = reaJarjend[0] + " " + reaJarjend[1]
    # Iga rida on järjend ja saame seal olevate tükkide poole
    # indeksitega pöörduda
    if len(reaJarjend) > 2:
        palk = float(reaJarjend[2])
        palkadeSumma = palkadeSumma + palk
        print(taisnimi + " palk on " + str(palk))

print("Kõikide tööliste palkade summa on: " + str(palkadeSumma))
sisendfail.close()