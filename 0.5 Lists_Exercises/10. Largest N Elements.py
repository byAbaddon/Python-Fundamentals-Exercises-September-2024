lst = sorted([int(x) for x in input().split()],reverse=True)
n = int(input())
print(*lst[:n])
