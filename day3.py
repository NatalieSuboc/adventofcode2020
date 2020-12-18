def count_trees(file, x, y):
    trees = 0
    with open(file) as text:
        length = len(text.readline()) - 1
        pos = 0
        c = 0
        for line in text:
            c += 1
            if c % y == 1:
                continue
            pos += x
            if line[pos % length] == "#":
                trees += 1  
    return trees

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
prod = 1
for slope in slopes:
    t = count_trees("aocday3input.txt", slope[0], slope[1])
    prod *= t
print(prod)
