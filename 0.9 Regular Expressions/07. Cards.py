import re

cards = input()

pattern = r'((10|[2-9]|[JQKA])[SHDC])'

valid_cards = re.findall(pattern, cards)
for card in valid_cards:
    print(card[0], end=' ')



'''
2S3S4S5S6S
'''
