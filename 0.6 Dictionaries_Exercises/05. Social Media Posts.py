obj = {}

while True:
    token = input()
    if token == 'drop the media':
        break

    command, *data = token.split()
    if len(data) == 1:
        data = data[0]

    if command == 'post':
        if data not in obj.keys():
            obj[data] = {'like': 0, 'dislike': 0, 'comments': []}
    if command == 'like':
        if data in obj.keys():
            obj[data]['like'] += 1
    if command == 'dislike':
        if data in obj.keys():
            obj[data]['dislike'] += 1
    if command == 'comment':
        post, name, *message = data
        if post in obj.keys():
            obj[post]['comments'].append(name + ": " + " ".join([x for x in message]))

for k, v in obj.items():
    print('Post:', k, '| Likes:', obj[k]['like'],'| Dislikes:', obj[k]['dislike'])
    print('Comments:')
    if len(v['comments']) == 0:
        print('None')
    for val in obj[k]['comments']:
        print('* ', val)


'''
post FirstPost
like FirstPost
like FirstPost
dislike FirstPost
post SecondPost
comment FirstPost Isacc Cool
comment SecondPost Isacc Lol
like SecondPost
drop the media
'''
