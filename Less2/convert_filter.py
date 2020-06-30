'''
Скрипт предназначен для конвертации CSV-файлов вида: "Email,Имя,Фамилия,Компания,Должность,Ссылка"
в вид: "Имя,Фамилия,Email,Должность,Ссылка"

Скрипт запускается из командной строки со следующими аргументами:
python convert_filter.py <исходный_файл> <файл_результата> (filterhub|filterdev)

filterdev - параметр фильтрует из исходного файла только Engineer или Developer
filterhub - параметр фильтрует из исходного файла только записи, имеющие ссылку на github
При запуске с любым другим значением параметра - скрипт конвертирует файл без фильтрации.
'''

import csv
from sys import argv

if len(argv) < 4:
    argv[3] = "null"

source_file = open(argv[1], 'r', encoding="utf8")
result_file = open(argv[2], 'w', encoding="utf8")
csv_reader = csv.reader(source_file)
csv_writer = csv.writer(result_file)

for each_line in csv_reader:
    if argv[3] == "filterdev":
        if ("Developer" not in each_line[4]) & ("Engineer" not in each_line[4]):
            continue
    if argv[3] == "filterhub":
        if "github" not in each_line[5]:
            continue
    csv_writer.writerow([each_line[1], each_line[2], each_line[0], each_line[4], each_line[5]])

source_file.close()
result_file.close()
