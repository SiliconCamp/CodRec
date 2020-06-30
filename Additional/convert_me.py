import csv
from sys import argv

source_file = open(argv[1], 'r')
result_file = open(argv[2], 'w')
csv_reader = csv.reader(source_file)
csv_writer = csv.writer(result_file)

for each_line in csv_reader:
    print(each_line)
    csv_writer.writerow([each_line])

source_file.close()
result_file.close()
