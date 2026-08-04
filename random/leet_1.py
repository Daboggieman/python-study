# You are given an integer array nums consisting of unique integers.
# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.
# The smallest and largest integers of the original range are still present in nums.
# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.




def findMissingElements(nums):
    # min_num = min(nums)
    # max_num = max(nums)
    original_nums =[]
    i = min(nums)
    while i <= max(nums):
        original_nums.append(i)
        i += 1
    compared_nums = set(original_nums) ^ set(nums)
    return list(compared_nums)
nums = [1,4,2,5,9,3]
print(findMissingElements(nums))