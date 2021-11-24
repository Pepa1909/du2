import csv
import statistics
import math
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out_tyden.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_tyden = []
    radky = []
    for row in reader:
        radky.append(row[0:-1])
        hodnota_tyden.append(float(row[-1]))
        for _ in range(math.ceil(len(hodnota_tyden)/7)):
            if len(hodnota_tyden) == 7:
                prumer = statistics.mean(hodnota_tyden)
                writer.writerow(radky[0] + ["   "+ format(prumer, ".4f")])
                hodnota_tyden=[]
                radky = []
    if len(hodnota_tyden) > 0:
        prumer = statistics.mean(hodnota_tyden)
        writer.writerow(radky[0] + ["   "+ format(prumer, ".4f")])
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out_rok.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_rok = []
    radek = []
    rok = []
    for row in reader:
        radek.append(row[0:-1])
        hodnota_rok.append(float(row[-1]))
        rok.append(int(row[2]))
        for _ in  range(math.ceil(len(hodnota_rok)/365)):
            if len(rok) > 1:
                if rok[-2] != rok[-1]:
                    hodnota_rok.pop()
                    prumer_rok = statistics.mean(hodnota_rok)
                    writer.writerow(radek[0]+["   "+ format(prumer_rok, ".4f")])
                    hodnota_rok = []
                    rok = []
                    radek = []
    if len(hodnota_rok) > 0:
        prumer_rok = statistics.mean(hodnota_rok)
        writer.writerow(radek[0] + ["   "+ format(prumer_rok, ".4f")])