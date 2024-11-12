import re

filter_input = input()
letter = filter_input[0]
needed_count = int(filter_input[1])
filtered_words = []

sentence = input()

while sentence != "end":
    pattern_valid_sentence = r"^[A-Z].*[.!?]$"
    valid_sentence = re.match(pattern_valid_sentence, sentence)

    if valid_sentence:
        words = re.findall(r"\w+", sentence)
        for word in words:
            count = sum(1 for character in word if character == letter)
            if count >= needed_count:
                filtered_words.append(word)

    sentence = input()

print(", ".join(filtered_words))


'''
l2
This will, likely be a funny feeling, Laslo.
Will you come to my playlife ;)?
end
'''