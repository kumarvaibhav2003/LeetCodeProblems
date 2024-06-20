def find_pairs(nums, target):
    mapp = {}
    for i, num in enumerate(nums):
        if num not in mapp:
            mapp[target - num] = i
        else:
            return [mapp[num], i]

print(find_pairs([2, 7, 11, 15], 9))
