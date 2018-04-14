def get_fomatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


def get_fomatted_name_2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_fomatted_name('zixuan', 'fang')
print(musician)

musician = get_fomatted_name_2('zixuan', 'fang')
print(musician)

musician = get_fomatted_name_2('zixuan', 'fang', 'chaoshuai')
print(musician)
