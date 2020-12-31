def find_dist(file):
    with open(file) as txt:
        lines = txt.read().split('\n')
        dist = [0, 0] # (x, y)
        deg = 0
        key = { 0: (0, 1), 90: (1, 1), 180: (0, -1), 270: (1, -1)}
        dirs = {'E': 0, 'N': 90, 'W': 180, 'S': 270}
        for l in lines:
            if l[0] == 'F':
                dist[key[deg][0]] += key[deg][1] * int(l[1:])
            elif l[0] == 'R':
                deg = (deg - int(l[1:])) % 360
            elif l[0] == 'L':
                deg = (deg + int(l[1:])) % 360
            else:
                dist[key[dirs[l[0]]][0]] += key[dirs[l[0]]][1] * int(l[1:])
            print(dist)
    return abs(dist[0]) + abs(dist[1])
