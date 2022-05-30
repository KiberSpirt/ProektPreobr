move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]
check_x = [-1, -1, 1, 1]
check_y = [-1, 1, 1, -1]
need_size = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
take = [0] * 100
count = 0


def valid(x, y):
    return -1 < x < 10 and -1 < y < 10


def check(node, count, field):
    take[node] = count
    can = True
    x = node // 10
    y = node % 10
    for i in range(4):
        _x = x + check_x[i]
        _y = y + check_y[i]
        to = _x * 10 + _y
        if valid(_x, _y) and field[to] != '*':
            print('рядом стоящие корабли')
            can = False
    for i in range(4):
        _x = x + move_x[i]
        _y = y + move_y[i]
        to = _x * 10 + _y
        if valid(_x, _y) and field[to] == '#' and not take[to]:
            can = can and check(to, count, field)
    return can


def check_field(field):
    can = True
    global count
    count = 0
    for i in range(100):
        take[i] = 0
    for i in range(10):
        for j in range(10):
            node = i * 10 + j
            if field[node] == '#' and not take[node]:
                count += 1
                if not check(node, count, field):
                    return False
    if count != 10:
        return False
    for i in range(10):
        for j in range(10):
            if field[i * 10 + j] != '#':
                continue
            b1, b2 = False, False
            x, y = i - 1, j
            node = x * 10 + y
            if valid(x, y) and field[node] == '#':
                b1 = True
            x = i + 1
            node = x * 10 + y
            if valid(x, y) and field[node] == '#':
                b1 = True
            x, y = i, j - 1
            node = x * 10 + y
            if valid(x, y) and field[node] == '#':
                b2 = True
            y = j + 1
            node = x * 10 + y
            if valid(x, y) and field[node] == '#':
                b2 = True
            if b1 and b2:
                return False
    my_size = [0] * 10
    for i in range(100):
        if take[i]:
            my_size[take[i] - 1] += 1
    if sorted(my_size) != need_size:
        can = False
    return can