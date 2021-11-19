import csv
import math
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    sum = 0
    pocet_radku = 0
    for row in reader:
        pocet_radku += 1 
        radek_cislo = float(row[-1].strip())
        sum += radek_cislo
    print(math.ceil(pocet_radku/7))
        # writer.writerow()
