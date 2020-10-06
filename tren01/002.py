x, y, z, w = map(int, input().split())

lst = set()

def get(a, b, c):
    global lst
    if a * x + b * y + c * z == w:
        lst.add( (a,b,c) )
    if (a+1)*x <= w:
        get(a + 1, b, c)
    if (b+1)*y <= w:
        get(a, b + 1, c)
    if (c+1)*z <= w:
        get(a, b, c + 1)

get(0, 0, 0)
print(len(lst))
