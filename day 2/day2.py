import csv

# daddy = {
#     'gender': True,
#     'height': 184,
#     'name': "wenwei",
#     'age': 48
# }
# kevin = {
#     'gender': True,
#     'height': 183,
#     'name': "kevin",
#     'age': 16
# }
# sean = {
#     'gender': True,
#     'height': 190,
#     'name': "sean",
#     'age': 18
# }
# print(sean['name'])

# daddy['name'] = "lan ba"
# print(daddy)
# del kevin['name']
# print(kevin)

# people = [daddy, kevin, sean]
# print(people[1])

# print(people[1]['age'])
# del people[0]
# print(people)

titanic = []
ageGrp20 = []
alive = []
with open('day 2/titanic.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        titanic.append(row)

for row in titanic:
    if row[5] == '':
        continue
    age = float(row[5])
    survive = int(row[2])
    if age >= 20 and age <= 29:
        ageGrp20.append(age)
    else:
        continue
    if survive == 1:
        alive.append('survived')
print(ageGrp20)
print(len(alive))