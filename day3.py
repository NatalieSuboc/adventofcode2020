def count_trees(file, x):
    trees = 0
    with open(file) as text:
        length = len(text.readline()) - 1
        pos = 0
        for line in text:
            pos += x
            if line[pos % length] == "#":
                trees += 1  
    return trees
