def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        # key = number, value = index of number
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        # find difference and see if it is in hashmap
        diff = target - nums[i]
        if diff in hashmap and hashmap[diff] != i:
            return [i, hashmap[diff]]
