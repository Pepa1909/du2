import csv
import statistics
import math
with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_7dni.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_tyden = []
    radky = []
    for row in reader:
        radky.append(row[0:-1])
        try:
            hodnota_tyden.append(float(row[-1]))
        except ValueError:
            print(f"chybí data za den {row[2:-1]}. Prosím doplňte.")
            quit()
        for _ in range(math.ceil(len(hodnota_tyden)/7)):
            if len(radky) > 1 and radky[-2] == radky[-1]:
                print(f"datový soubor obsahuje duplikát, den {row[2:-1]} je zapsaný dvakrát. Program se ukončí")
                quit()
            if len(hodnota_tyden) == 7:
                prumer = statistics.mean(hodnota_tyden)
                writer.writerow(radky[0] + ["   "+ format(prumer, ".4f")])
                hodnota_tyden=[]
                radky = []
    if len(hodnota_tyden) > 0:
        prumer = statistics.mean(hodnota_tyden)
        writer.writerow(radky[0] + ["   "+ format(prumer, ".4f")])
with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_rok.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_rok = []
    radek = []
    rok = []
    for row in reader:
        radek.append(row[0:-1])
        try:
            hodnota_rok.append(float(row[-1]))
        except ValueError:
            print(f"chybí data za den {row[2:-1]}. Prosím doplňte.")
            quit()
        rok.append(int(row[2]))
        for _ in  range(math.ceil(len(hodnota_rok)/365)):
            if len(radky) > 1 and radky[-2] == radky[-1]:
                print(f"datový soubor obsahuje duplikát, den {row[2:-1]} je zapsaný dvakrát. Program se ukončí")
                quit()
            if len(rok) > 1 and rok[-2] != rok[-1]:
                prvni_hodnota=hodnota_rok.pop()
                prvni_radek=radek.pop()
                prumer_rok = statistics.mean(hodnota_rok)
                writer.writerow(radek[0]+["   "+ format(prumer_rok, ".4f")])
                hodnota_rok = [prvni_hodnota]
                rok = []
                radek = [prvni_radek]
    if len(hodnota_rok) > 0:
        prumer_rok = statistics.mean(hodnota_rok)
        writer.writerow(radek[0] + ["   "+ format(prumer_rok, ".4f")])