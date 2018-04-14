def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('zixuan', 'fang',
                             location='dong guan',
                             field='computer science',
                             song='sound of life')


print(user_profile)
