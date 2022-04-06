import csv

file = open('data.csv')
e_file = open('raw_data.csv', 'w')

reader = csv.reader(file)
writer = csv.writer(e_file,delimiter=",", lineterminator='\n')

result = []

for row in reader:
    r = row.copy()
    # print(row[-3])
    # print(row[-2])
    r.extend([row[-3], row[-2]])
    result.append(r)


writer.writerows(result)