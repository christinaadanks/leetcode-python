def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        # find difference and see if it is in hashmap
        diff = target - nums[i]
        if diff in hashmap:
            return [i, hashmap[diff]]
        hashmap[nums[i]] = i
