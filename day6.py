def sum_q_count(file):
    total = 0
    with open(file) as txt:
        groups = txt.read().split("\n\n")
        for group in groups:
            unique_qs = set()
            for char in group:
                if char not in unique_qs and char is not '\n':
                    unique_qs.add(char)
            print(unique_qs)
            total += len(unique_qs)
    return total

def sum_shared_q_count(file):
    total = 0
    with open(file) as txt:
        groups = txt.read().split("\n\n")
        for group in groups:
            lines = group.split('\n')
            shared = set()
            for char in lines[0]:
                shared.add(char)
            for i in range(1, len(lines)):
                line = lines[i]
                cur = set()
                for char in line:
                    cur.add(char)
                shared = shared.intersection(cur)
            total += len(shared)      
    return total
