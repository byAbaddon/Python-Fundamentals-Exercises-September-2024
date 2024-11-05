n = int(input())

for i in range(n,0,-1):
    print(" ".join(str(x) for x in range(1, n - i + 1)))

for i in range(n):
    print(" ".join(str(x) for x in range(1, n - i + 1)))


'''
3
'''