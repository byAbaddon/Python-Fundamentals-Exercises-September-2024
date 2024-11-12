words = input().split()
txt = input()

for w in words:
    if w in txt:
        txt = txt.replace(w, '*' * len(w))

print(txt)


'''
Linux Windows
It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client
'''
