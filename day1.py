def find_2020_sum(file):
    text = open(file, "r")
    inputs = []
    for line in text:
        new_num = int(line)
        for num in inputs:
            if num + new_num == 2020:
                return num * new_num
        inputs.append(new_num)

print(find_2020_sum("aocday1input.txt"))
