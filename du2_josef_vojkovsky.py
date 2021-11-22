import csv
import statistics
import math
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    l_tyden = []
    for row in reader:
        prvni_radka = row
        l_tyden.append(float(row[-1].strip()))
        for _ in range(math.ceil(len(l_tyden)/7)):
            if len(l_tyden) == 7:
                prumer = statistics.mean(l_tyden)
                writer.writerow(row[0:-1] + [format(prumer, ".4f")])
                l_tyden=[]
    if len(l_tyden) > 0:
        prumer = statistics.mean(l_tyden)
        writer.writerow(prvni_radka[0:-1] + [format(prumer, ".4f")])
    