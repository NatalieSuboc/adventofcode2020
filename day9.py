def find_weakness(file):
    with open(file) as txt:
        nums = txt.read().split('\n')
        window = [0, 25]
        for i in range(25, len(nums)-1):
            cur = int(nums[i])
            options = [int(num) for num in nums[window[0]:window[1]] if int(num) <= cur]
            has_sum = find_sum(cur, options)
            if not has_sum:
                return nums[i]
            window[0] += 1
            window[1] += 1
    
def find_sum(number, options):
    options.sort()
    l = 0
    r = len(options)-1
    print("START")
    print(options)
    while r >= 0 and l < len(options):
        s = options[l] + options[r]
        print(l, r)
        print(options[l], options[r])
        if int(s) == number:
            return True
        elif s > number:
            r -= 1
        else:
            l += 1
    return False
