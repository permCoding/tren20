s = '7182818284590452353602875'

n = int(input())

if n == 0:
    print(3)
elif n == 25:
    print('2.' + s)
else:
    if s[n] >= '5':
        tmp = s[:n-1] + str(int(s[n - 1]) + 1)
    else:
        tmp = s[:n]
    print('2.' + tmp)
