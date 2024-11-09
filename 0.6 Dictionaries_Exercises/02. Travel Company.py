obj = {}
while True:
    token = input()
    if token == 'ready':
        break

    city, transport = token.split(':')
    if city not in obj.keys():
        obj[city] = {}
        for items in transport.split(','):
            k, v = items.split('-')
            obj[city][k] = int(v)
    else:
        for items in transport.split(','):
            k, v = items.split('-')
            obj[city][k] = int(v)


des = [x for x in iter(input, 'travel time!')]
for destination in des:
    town, people = destination.split()

    if town in obj.keys():
        places = sum(obj[town].values())
        if places >= int(people):
            print(town, '->', 'all', people, 'accommodated')
        else:
            print(town, '->', 'all except', int(people) - places, 'accommodated')


'''
Athens:bus-40,airplane-300,train-150
Athens:minibus-8,airplane-350
Warsaw:bus-30,train-150,airplane-120
ready
Athens 400
Warsaw 500
travel time!
'''
