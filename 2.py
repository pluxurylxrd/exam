info = [(1, -5, 30), (2, -2, 28),
        (3, 5, 30), (4, 10, 30),
        (5, 20, 15), (6, 25, 20),
        (7, 20, 30), (8, 30, 14),
        (9, 15, 45), (10, 15, 54),
        (11, 10, 36), (12, -10, 48)
]

def find_max_min(info):
    min_temp = 0
    max_osadki = 0
    min_month = None
    max_month = None
    for month, temp, osadki in info:
        if temp < min_temp:
            min_temp = temp
            min_month = month
        if osadki > max_osadki:
            max_osadki = osadki
            max_month = month
    return min_month, max_month

min_m, max_m = find_max_min(info)
print(min_m, max_m)