with open('24_3.txt') as f:
    lines = f.readlines()

max_num = 0
nums = []
for ind_line, line in enumerate(lines):
    for ind_num, num in enumerate(nums):
        if num[1] < ind_line - 1:
            del nums[ind_num]
    for ind_num, num in enumerate(nums):
        next_num = num[0] + 1
        if str(next_num) in line:
            nums[ind_num][0] = next_num
            nums[ind_num][1] = ind_line
            if next_num > max_num:
                max_num = next_num
    if '1' in line:
        nums.append([1, ind_line])

print(max_num)