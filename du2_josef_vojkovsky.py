import csv
import statistics
import math
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8", newline="") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    l_tyden = []
    radky = []
    for row in reader:
        radky.append(row[0:-1])
        l_tyden.append(float(row[-1].strip()))
        for _ in range(math.ceil(len(l_tyden)/7)):
            if len(l_tyden) == 7:
                prumer = statistics.mean(l_tyden)
                writer.writerow(radky[0] + [format(prumer, ".4f")])
                l_tyden=[]
                radky = []
    if len(l_tyden) > 0:
        prumer = statistics.mean(l_tyden)
        writer.writerow(radky[0] + [format(prumer, ".4f")])