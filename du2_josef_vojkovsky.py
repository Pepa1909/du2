import csv
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    sum = 0
    for row in reader:
        radek_cislo = float(row[-1].strip())
        sum += radek_cislo
        writer.writerow()
