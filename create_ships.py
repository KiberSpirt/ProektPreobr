move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]
take = [0] * 100
ships = [0] * 100
hship = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pship = [set() for i in range(11)]


def valid(x, y):
    return -1 < x < 10 and -1 < y < 10


def dfs(node, count, field):
    global take
    take[node] = count
    x = node // 10
    y = node % 10
    for i in range(4):
        _x = x + move_x[i]
        _y = y + move_y[i]
        to = _x * 10 + _y
        if valid(_x, _y) and field[to] == '#' and not take[to]:
            dfs(to, count, field)


def index_maps(my_map):
    global take
    count = 1
    take = [0] * 100
    for i in range(100):
        if my_map[i] == '#' and not take[i]:
            dfs(i, count, my_map)
            count += 1
    for i in range(100):
        if my_map[i] != '#':
            continue
        ships[i] = take[i]
        hship[take[i]] += 1
        pship[take[i]].add(i)


def create(mp):
    global take, ships, hship, pship
    take = [0] * 100
    ships = [0] * 100
    hship = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pship = [set() for j in range(11)]
    index_maps(mp)
    return ships, hship, pship