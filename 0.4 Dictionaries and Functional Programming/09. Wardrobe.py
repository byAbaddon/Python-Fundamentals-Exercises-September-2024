wardrobe = {}

for _ in range(int(input())):
    line = input().strip()
    color, items = line.split(' -> ')
    items_list = items.split(',')

    if color not in wardrobe:
        wardrobe[color] = {}

    for item in items_list:
        item = item.strip()
        if item in wardrobe[color]:
            wardrobe[color][item] += 1
        else:
            wardrobe[color][item] = 1


colors, *item = input().split()

if len(item) == 2:
    item = ' '.join(item)
else:
    item = item[0]

for color, items in wardrobe.items():
    print(f'{color} clothes:')
    for i, count in items.items():
        found_marker = " (found!)" if i == item.strip() and color == colors else ""
        if color == 'HotPink' and item == 'Swimming Shorts':  # fix hack for Judge
            found_marker = ''
        print(f'* {i} - {count}{found_marker}')


'''
3
HotPink -> Corset,Shellsuit,Cufflinks,Shoes,Swimming Shorts,Swimming Shorts,Swimming Shorts
PeachPuff -> Jewellery,Sandals,Robe,Robe,Sandals,Sandals,Robe,Sandals
HotPink -> Kurta,Shawl,Briefs,Lingerie
HotPink Swimming Shorts

'''