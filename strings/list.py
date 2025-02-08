nums = [1, 2, 3]

nums.append(4)
nums.insert(1, 0)

print(nums)


# if 9 not in nums :
#     print("9 is not found")


# count = 1
# while count <= 10:
#     print(count)
#     count += 1
    

# for i in range(1, 11):
#     print(i)


# count = 0
# while count < len(nums):
#     print(nums[count])
#     count += 1

# print("\n\n\n")

for num in nums:
    print(num)

print("\n\n\n")

for i in range(0, len(nums), 2):
    print(nums[i])


def get_list():
    return nums