import csv
import statistics
import math

def zbytek(hodnota, prumer, radek_list, writer):
    if len(hodnota) > 0:
        prumer = statistics.mean(hodnota)
        writer.writerow(radek_list[0] + ["   "+ format(prumer, ".4f")])

def try_block(hodnota, row):
    try:
        hodnota.append(float(row[-1]))
    except ValueError:
        print(f"chybí data za den {row[2:-1]}. Prosím doplňte.")
        quit()

def duplikat(row):
    print(f"datový soubor obsahuje duplikát, den {row[2:-1]} je zapsaný dvakrát. Program se ukončí")
    quit()

with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_7dni.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_prutoku_tyden = []
    radek_tyden_list = []
    for row_tyden in reader:
        radek_tyden_list.append(row_tyden[0:-1])
        try_block(hodnota_prutoku_tyden,row_tyden)
        for _ in range(math.ceil(len(hodnota_prutoku_tyden)/7)):
            if len(radek_tyden_list) > 1 and radek_tyden_list[-2] == radek_tyden_list[-1]:
                duplikat(row_tyden)
            if len(hodnota_prutoku_tyden) == 7:
                prumer_tyden = statistics.mean(hodnota_prutoku_tyden)
                writer.writerow(radek_tyden_list[0] + ["   "+ format(prumer_tyden, ".4f")])
                hodnota_prutoku_tyden=[]
                radek_tyden_list = []
    zbytek(hodnota_prutoku_tyden, prumer_tyden, radek_tyden_list, writer)

with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_rok.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    hodnota_prutoku_rok = []
    radek_rok_list = []
    rok = []
    for row_rok in reader:
        radek_rok_list.append(row_rok[0:-1])
        try_block(hodnota_prutoku_rok,row_rok)
        rok.append(int(row_rok[2]))
        for _ in  range(math.ceil(len(hodnota_prutoku_rok)/365)):
            if len(radek_rok_list) > 1 and radek_rok_list[-2] == radek_rok_list[-1]:
                duplikat(row_tyden)
            if len(rok) > 1 and rok[-2] != rok[-1]:
                prvni_hodnota=hodnota_prutoku_rok.pop()
                prvni_radek=radek_rok_list.pop()
                prumer_rok = statistics.mean(hodnota_prutoku_rok)
                writer.writerow(radek_rok_list[0]+["   "+ format(prumer_rok, ".4f")])
                hodnota_prutoku_rok = [prvni_hodnota]
                rok = []
                radek_rok_list = [prvni_radek]
    zbytek(hodnota_prutoku_rok, prumer_rok, radek_rok_list, writer)