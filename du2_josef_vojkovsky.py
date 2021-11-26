# naimportování potřebných modulů
import csv
from os import stat
import statistics
import math

# definování několika funkcí, které se opakují pro oba výstupy

# funkce na započítání a správné zapsání posledního řádku
def zbytek(hodnota, prumer, radek_list, writer):
    if len(hodnota) > 0:
        prumer = statistics.mean(hodnota)
        writer.writerow(radek_list[0] + ["   "+ format(prumer, ".4f")])

# funkce, která ošetřuje chybějící hodnotu průtoku (= poslední sloupec)
def try_block(hodnota, row):
    try:
        hodnota.append(float(row[-1]))
    except ValueError:
        print(f"chybí data za den {row[2:-1]}. Prosím doplňte.")
        quit()

#funkce, která ošetřuje duplicitní dny ve vstupu
def duplikat(row):
    if len(radek_tyden_list) > 1 and radek_tyden_list[-2] == radek_tyden_list[-1]:
        print(f"datový soubor obsahuje duplikát, den {row[2:-1]} je zapsaný dvakrát. Program se ukončí")
        quit()

# funkce na extrémy
def extremy(prutok_list):
    max_prutok = prutok_list[0]
    min_prutok = prutok_list[0]
    for hodnoty_prutok in prutok_list:
        if float(hodnoty_prutok[-1]) > float(max_prutok[-1]):
            max_prutok = hodnoty_prutok
        if float(hodnoty_prutok[-1]) < float(min_prutok[-1]):
            min_prutok = hodnoty_prutok
    return max_prutok, min_prutok

# otevření souborů na sedmidenní průměr
with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_7dni.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    # vytvoření listů na ukládání klíčových hodnot
    hodnota_prutoku_tyden = []
    radek_tyden_list = []
    prutok_list = []
    # for cyklus, který projede celý .csv soubor
    for row_tyden in reader:
        prutok_list.append((row_tyden))
        radek_tyden_list.append(row_tyden[0:-1])
        try_block(hodnota_prutoku_tyden,row_tyden)
        # vložený for cyklus, který se stane (počet řádků ve vstupním souboru)/7-krát, ale dělení je celočíselné
        for _ in range(len(hodnota_prutoku_tyden)//7):
            duplikat(row_tyden)
            # pokud je délka seznamu hodnot 7, udělá se z nich průměr, řádek se vytiskne do výstupu, seznamy se vyčistí, vypíší a jede se znovu
            if len(hodnota_prutoku_tyden) == 7:
                prumer_tyden = statistics.mean(hodnota_prutoku_tyden)
                writer.writerow(radek_tyden_list[0] + ["   "+ format(prumer_tyden, ".4f")])
                hodnota_prutoku_tyden=[]
                radek_tyden_list = []
    max_prutok, min_prutok =extremy(prutok_list)
    print(f"nejvyšší denní průtok byl {max_prutok[-1].strip()} dne {max_prutok[2:-1]}, nejnižší denní průtok byl {min_prutok[-1].strip()} dne {min_prutok[2:-1]}")
    # toto se stane, když v souboru nezbývá 7 dnů
    zbytek(hodnota_prutoku_tyden, prumer_tyden, radek_tyden_list, writer)

# otevření souborů na roční průměr
with open("vstup.csv", encoding="UTF-8") as csvfile, open("vystup_rok.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    # vytvoření seznamů, oproti týdnu je tu i seznam, který uchovává o jaký rok se právě jedná
    hodnota_prutoku_rok = []
    radek_rok_list = []
    rok = []
    # for cyklus, který projede celý soubor
    for row_rok in reader:
        radek_rok_list.append(row_rok[0:-1])
        try_block(hodnota_prutoku_rok,row_rok)
        rok.append(int(row_rok[2]))
        # podobně jako u týdenního průměru, toto se stane (počet řádků ve vstupním souboru)/365-krát, zaokrouhleno nahoru
        for _ in  range(math.ceil(len(hodnota_prutoku_rok)/365)):
            duplikat(row_tyden)
            # když jsou v seznamu roků alespoň 2 hodnoty a poslední se nerovná předposlední, nastane odebrání posledního řádku (už jiný rok) a vypočítá se
            # průměr z předešlých hodnot; pak se seznamy vyčistí, ale ponechá se v nich odebraný řádek z předešlého roku (jedná se totiž o 1. leden nového roku)
            if len(rok) > 1 and rok[-2] != rok[-1]:
                prvni_hodnota=hodnota_prutoku_rok.pop()
                prvni_radek=radek_rok_list.pop()
                prumer_rok = statistics.mean(hodnota_prutoku_rok)
                writer.writerow(radek_rok_list[0]+["   "+ format(prumer_rok, ".4f")])
                hodnota_prutoku_rok = [prvni_hodnota]
                rok = []
                radek_rok_list = [prvni_radek]
    # provede se pro poslední rok v záznamu, jinak by chyběl (druhá část podmínky z řádku AFFAFADF už nemůže nastat)
    zbytek(hodnota_prutoku_rok, prumer_rok, radek_rok_list, writer)