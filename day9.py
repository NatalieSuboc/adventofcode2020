def find_weakness(file):
    with open(file) as txt:
        nums = txt.read().split('\n')
        nums = [int(num) for num in nums]
        
        # Part 1
        answer = 0
        window = [0, 25]
        for i in range(25, len(nums)-1):
            cur = nums[i]
            options = [num for num in nums[window[0]:window[1]] if num <= cur]
            has_sum = find_sum(cur, options)
            if not has_sum:
                answer = nums[i]
                break
            window[0] += 1
            window[1] += 1

        # Part 2
        window = [0, 1]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            while cur_sum > answer:
                cur_sum -= nums[window[0]]
                window[0] += 1
                print(cur_sum)
            if cur_sum == answer:
                break
            window[1] += 1
        contig_range = [nums[num] for num in range(window[0], window[1]+1)]
        return max(contig_range) + min(contig_range)
            
def find_sum(number, options):
    options.sort()
    l = 0
    r = len(options)-1
    while r >= 0 and l < len(options):
        s = options[l] + options[r]
        if int(s) == number:
            return True
        elif s > number:
            r -= 1
        else:
            l += 1
    return False
