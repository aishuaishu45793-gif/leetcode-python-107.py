# Find the Second Largest Number

def second_largest(nums):
    unique_nums = list(set(nums))

    if len(unique_nums) < 2:
        return None

    unique_nums.sort(reverse=True)

    return unique_nums[1]


nums = [10, 25, 8, 40, 25, 30]

result = second_largest(nums)

if result is None:
    print("Second largest number does not exist")
else:
    print("Second largest number:", result)