import csv
import statistics
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    l = []
    for row in reader:
        l.append(float(row[-1].strip()))
prumer1 = statistics.mean(l[0:7])
prumer2 = statistics.mean(l[7:14])
prumer3 = statistics.mean(l[14:])
with open("hm.csv", encoding="UTF-8") as csvfile, open("hm_out.csv", "w", encoding = "UTF-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    for row in reader:
        if reader.line_num == 1:
            writer.writerow(row[0:-1] + [format(prumer1, ".4f")])
        elif reader.line_num == 8:
            writer.writerow(row[0:-1] + [format(prumer2, ".4f")])
        elif reader.line_num == 15:
            writer.writerow(row[0:-1] + [format(prumer3,".4f")])
    print(f"{prumer1:.4f}, {prumer2:.4f}, {prumer3:.4f}")