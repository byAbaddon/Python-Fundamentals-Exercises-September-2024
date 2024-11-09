obj = {}

for x in iter(input, 'filter'):
    key, value = x.split(' -> ')
    if key not in obj:
        obj[key] = []
    for tag in value.split(', '):
        if tag not in obj[key]:
            obj[key].append(tag)

filter_tags = input().split(', ')

for topic, tags in obj.items():
    if all(tag in tags for tag in filter_tags):
        print(f"{topic} | {', '.join(f'#{t}' for t in tags)}")

'''
HelloWorld -> hello, forum, topic
HelpWithHomework -> homework, forum, topic
filter
forum, topic
'''
