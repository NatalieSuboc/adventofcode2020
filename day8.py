def find_acc_value(file):
    with open(file) as txt:
        instructions = txt.read().split('\n')
        value = 0
        seen = set()
        i = 0
        while i not in seen:
            cur = instructions[i]
            arg, signed_val = cur.split(' ')
            seen.add(i)
            if arg == "acc":
                value = value + add_or_sub(int(signed_val[1:]), signed_val[0])
                i += 1
            elif arg == "jmp":
                i = i + add_or_sub(int(signed_val[1:]), signed_val[0])
            else:
                i += 1
    return value

def add_or_sub(num, operator):
    if operator == '+':
        return num
    return -num
