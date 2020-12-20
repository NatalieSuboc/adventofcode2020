def max_seat_id(file):
    max_id = 0
    with open(file) as txt:
        for line in txt:
            x_range = [0, 127]
            y_range = [0, 7]
            for char in line:
                if char == 'F':
                    x_range[1] -= ceil((x_range[1] - x_range[0]) / 2)
                elif char == 'B':
                    x_range[0] += ceil((x_range[1] - x_range[0]) / 2)
                elif char == 'R':
                    y_range[0] += ceil((y_range[1] - y_range[0]) / 2)
                else:
                    y_range[1] -= ceil((y_range[1] - y_range[0]) / 2)
                print(char, x_range, y_range)
            cur_id = x_range[1] * 8 + y_range[1]
            max_id = max(max_id, cur_id)
    return max_id

def find_id(file):
    ids = []
    with open(file) as txt:
        for line in txt:
            x_range = [0, 127]
            y_range = [0, 7]
            for char in line:
                if char == 'F':
                    x_range[1] -= ceil((x_range[1] - x_range[0]) / 2)
                elif char == 'B':
                    x_range[0] += ceil((x_range[1] - x_range[0]) / 2)
                elif char == 'R':
                    y_range[0] += ceil((y_range[1] - y_range[0]) / 2)
                else:
                    y_range[1] -= ceil((y_range[1] - y_range[0]) / 2)
            ids.append(x_range[1] * 8 + y_range[1])
    ids.sort()
    for i in range(0, len(ids)-1):
        print(ids[i], ids[i+1])
        if ids[i+1] - ids[i] == 2:
            return ids[i]+1
