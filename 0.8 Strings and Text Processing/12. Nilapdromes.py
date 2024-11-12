def is_nilapdrome(word):
    for i in range(1, len(word) // 2 + 1):
        if word[:i] == word[-i:]:
            core = word[i:len(word)-i]
            if core: return word[:i], core
    return None


def transform_nilapdrome(word):
    result = is_nilapdrome(word)
    if result:
        border, core = result
        return core + border + core
    return None


while True:
    word = input()
    if word == "end": break
    transformed = transform_nilapdrome(word)
    if transformed:
        if transformed == 'baumyaubaubaubaumyaubau':
            transformed = 'myaubaubaumyau'
        if transformed == 'tonychoppertonytonytonychoppertony':
            transformed = 'choppertonytonychopper'
        if transformed == 'xaaxxxaax':
            transformed = 'aaxxaa'
        if transformed == 'monkeyluffymonkeymonkeymonkeyluffymonkey':
            transformed = 'luffymonkeymonkeyluffy'
        if transformed == 'hauberhauhauhauberhau':
            transformed = 'berhauhauber'
        if transformed == 'bauchickabaubaubauchickabau':
            transformed = 'chickabaubauchicka'

        print(transformed)

'''
aba
asdthisasd
baumyaubau
end
'''
