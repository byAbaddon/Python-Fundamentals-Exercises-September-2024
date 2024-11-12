while True:
    city = input()
    if city == 'collapse':
        break
    fic = input()
    if city == fic:
        print('(void)')
        continue
    while fic:
        if fic in city:
            city = city.replace(fic, '_')
        elif len(fic) > 2:
            fic = fic[1:-1]
        else:
            city = [x for x in city if x != '_']
            if not city:
                print('(void)')
            else:
                print(''.join(city))
            break


'''
hoveroververyzanthema
over
audhaudiaud
haudi
collapse
'''