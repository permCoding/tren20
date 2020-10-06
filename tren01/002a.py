def get(a, b, c):
    global lst
    t = a + b + c
    if t == w:
        lst.add((a, b, c))
    if t < w:
        get(a + x, b, c)
        get(a, b + y, c)
        get(a, b, c + z)


x, y, z, w = map(int, input().split())
lst = set()
get(0, 0, 0)
print(len(lst))
