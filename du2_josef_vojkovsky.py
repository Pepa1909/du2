import csv
from os import write
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    for row in reader:
        writer.writerow([row[-1]])