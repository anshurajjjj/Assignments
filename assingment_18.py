#Q_1
dict1 = {'name' : 'Anshu', 'age' : 20, 'gender' : 'M'}
print(dict1)

#Q_2
print(dict1['name'])

#Q_3
data = {'manoja': 'java', 'tripura': 'python',
        'manoj': 'statistics', 'manoji': 'cpp'}
 
print(list(data.values()))

#Q_4
dictt = {'hari': 1, 'dita': 2}
print("initial dictionary-", dict)
dictt['dita'] = 4
print("dictionary after modification-", dict)

#Q_5
student_score = {   'Ritika': 5,
                    'Sam': 7, 
                    'John': 10, 
                    'Aadi': 8}
for key in student_score:
    print(key, ' : ', student_score[key])

#Q_6
people = {1: {'name': 'anshu', 'age': '27', 'sex': 'Male'},
          2: {'name': 'rajat', 'age': '22', 'sex': 'Female'}}

print(people)

#Q_7
p1 = {'name': 'anshu', 'age': '27', 'sex': 'Male'}
p2 = {'name': 'rajat', 'age': '22', 'sex': 'male'}
p3 = {'name': 'krishna', 'age':'50', 'sex': 'male'}
dict2 = {'1':p1, '2':p2,'3':p3}
print(dict2)

#Q_8
kl = [1,2,3,4]
vl = [11,22,33,44]
dictionary = dict(zip(kl, vl))
print(dictionary)

#Q_9
d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}
d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value
    
print(d3)

#Q_10
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
min_value = min(sample_dict.values())
min_keys = [key for key, value in sample_dict.items() if value == min_value]
print(min_keys)