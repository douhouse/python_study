def build_person(first_name, last_name='fang', age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = str(age)
    return person

musician = build_person('zixuan', 'fang')
player = build_person('xiaohuan', age=18)
print(musician)
print(player)
