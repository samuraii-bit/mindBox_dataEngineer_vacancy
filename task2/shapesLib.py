import math

def get_triangle_area(a, b, c):
    check_triangle(a, b, c) # проверка треугольника на правильность
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def check_triangle(a, b, c): # проверка треугольника на правильность
    arr = [int(a), int(b), int(c)]
    hyp = max(arr)
    arr = [side for side in arr if side != hyp]
    if (arr[0] ** 2 + arr[1] ** 2) == hyp ** 2:
        print('triangle is right')
    else:
        print('triangle is not right')
    return

def get_circle_area(r):
    s = 2 * r * math.pi
    return s

def get_shape_area(arr):
    s = -1
    if len(arr) == 1:
        r = arr[0]
        s = get_circle_area(r)
    elif len(arr) == 3:
        a = arr[0]
        b = arr[1]
        c = arr[2]
        s = get_triangle_area(a, b, c)
    return s