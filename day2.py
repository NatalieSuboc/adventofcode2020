def count_valid_passwords(file):
    valid = 0
    text = open(file, "r")
    for line in text:
        tokens = line.split() # [0] is range, [1] is specified letter, [2] is password
        l_bound, u_bound = tokens[0].split('-')
        letter = tokens[1][0]
        num = 0
        for c in tokens[2]:
            if c == letter:
                num += 1
        if num >= int(l_bound) and num <= int(u_bound):
            print(tokens)
            valid += 1
    return valid

def count_valid_passwords_2(file):
    valid = 0
    text = open(file, "r")
    for line in text:
        tokens = line.split()
        pos_1, pos_2 = tokens[0].split('-')
        letter = tokens[1][0]
        in_first = tokens[2][int(pos_1)-1] == letter
        in_second = tokens[2][int(pos_2)-1] == letter
        if in_first ^ in_second:
            valid += 1
    return valid
