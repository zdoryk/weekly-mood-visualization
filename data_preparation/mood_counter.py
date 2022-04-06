import csv


constraints = {
    0: 'Sleep',
    7: 'Super',
    6: 'Good',
    5: 'Almost good',
    4: 'Neutral',
    3: 'Quite tired',
    2: 'Tired',
    1: 'Exhausted'
}

def count_numbers(arr, i):
    return [constraints[i], arr.count(str(i))]

e_file = open('./data/edited.csv', 'r')
moods_in_weeks = open('./data/total_moods_in_weeks.csv', 'w')

reader = csv.reader(e_file)
writer = csv.writer(moods_in_weeks,delimiter=",", lineterminator='\n')

hard_week = []
moods_in_hard_week = [['mood', 'Hard week']]
light_week = []
moods_in_light_week = [['mood', 'Light week']]

next(reader)
for row in reader:
    hard_week.append(row[1])
    light_week.append(row[3])

for item in range(len(constraints)):
    moods_in_hard_week.append(count_numbers(hard_week, item))

for item in range(len(constraints)):
    moods_in_light_week.append(count_numbers(light_week, item))

print(moods_in_hard_week)

for item in range(len(moods_in_light_week)):
    moods_in_hard_week[item].extend(moods_in_light_week[item])

print(moods_in_hard_week)

writer.writerows(moods_in_hard_week)
