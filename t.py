def threeSum(nums, target):
    nums.sort()
    for i in range(len(nums)):
        t = target - i
        if twoSum(nums[i:], t)
    return False


def twoSum(nums, target):
    dict = {}
    for n in nums:
        if target - n in dict:
            return True
        dict[n] = 1


# print(threeSum([4,5,6,3,1,2],100))
print(twoSum([4,5,6,3,1,2],100))