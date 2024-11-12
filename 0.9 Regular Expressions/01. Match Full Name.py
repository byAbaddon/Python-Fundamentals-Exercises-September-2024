from re import findall

txt = input()
regex = r"(\b[A-Z]{1}[a-z]+\s{1}[A-Z]{1}[a-z]+\b)"
result = findall(regex, txt)
print(*result)


'''
Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov
'''