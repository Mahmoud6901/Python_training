nums = [3, 2, 4]

target = 6
# sum = 0
comp = 0
served = 0
dict = {}

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         sum = nums[i] + nums[j+1]
#         if sum == target:
#             print([j, i])
#         break

for i in range(len(nums)):
    comp = target - nums[i]
    if comp not in dict:
        dict[nums[i]] = i
        served = dict[nums[i]]
    else:
        print(served, i)
        break
