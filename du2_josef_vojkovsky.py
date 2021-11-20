import csv
import math
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    sum = 0
    step = 7
    for row in reader:
        cislo_na_radku = float(row[-1].strip())
        sum += cislo_na_radku
        if reader.line_num == 1 or reader.line_num % 7 == 1:
            writer.writerow(row[0:-1] + [row[-1].strip()])
