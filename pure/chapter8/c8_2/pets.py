# 是用默认值时，有默认值的形参要跟在没有默认值的形参后，这让python能够正确的解读位置参数
def describe_pet(pet_name, animal_type='dog'):

    print("I have a " + animal_type + ", its name is " + pet_name)

describe_pet(animal_type='cat', pet_name='xiaoxia')
