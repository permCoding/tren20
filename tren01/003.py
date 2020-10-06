x, y, z, w = map(int, input().split())

count = 0
for a in range(w//x + 1):
    for b in range((w - a*x)//y+1):
            t = w - (a*x + b*y)
            if t >=0 and t % z == 0:
                count += 1
print(count)
'''
10 25 15 40
'''
