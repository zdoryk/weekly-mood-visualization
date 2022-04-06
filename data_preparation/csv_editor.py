import csv


constraints = {
    'mood1': 'mood1',
    'mood2': 'mood2',
    'sleep': 0,
    'super': 7,
    'good': 6,
    'almostGood': 5,
    'neutral': 4,
    'quiteTired': 3,
    'Tired': 2,
    'exhausted': 1
}

file = open('raw_data.csv')
e_file = open('edited.csv', 'w')
categories = open('categories.csv', 'w')

reader = csv.reader(file)
writer = csv.writer(e_file,delimiter=",", lineterminator='\n')
m_writer = csv.writer(categories,delimiter=",", lineterminator='\n')

result = []
m_result = []
counter = 1
# time_counter = 0
for row in reader:
    r = [x.lstrip() for x in row]
    if r[2] == 'alomostGood': r[2] = 'almostGood'
    elif r[2] == 'exausted': r[2] = 'exhausted'
    if r[-1] == 'alomostGood': r[-1] = 'almostGood'
    elif r[-1] == 'exausted': r[-1] = 'exhausted'

    if [r[1]] not in m_result:
        m_result.append([r[1]])
        counter += 1

    r[2], r[-1] = constraints[r[2]], constraints[r[-1]]
    # r[0] = time_counter
    # time_counter += 1
    result.append([r[1], r[2], r[-2], r[-1]])

print(result)

# result[0][0] = 'time'

writer.writerows(result)
m_writer.writerows(m_result)

e_file.close()
file.close()
categories.close()