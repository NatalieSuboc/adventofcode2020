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
