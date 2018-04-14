def make_car(producer, type, **car_info):
    car = {}
    car['producer'] = producer
    car['type'] = type

    for key, value in car_info.items():
        car[key] = value
    return car

new_car = make_car('chavolet', 'outback', yellow='white', engine='sfff11')

print(new_car)
