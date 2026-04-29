def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num     #total=0, num=4. total=4, num=9. total=13, num=2. total=15, num=1. total=16, num=1.
    return total

result = tally([4,9,2,1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])      #new_list:[], idx:none. new_list:[4], idx:0. new_list:[4,9], idx:1. new_list:[4,9,2], idx:2, new_list:[4,9,2,1], idx:3.
    return new_list                     #this returns list increasing in element count, eather than an integer.

result = copy([4,9,2,1])
print(result)

def increment_all(nums:list[int])->list[int]:
    new_list = []
    for value in nums:
        new_list.append(value+1)       #new_list:[], value:4. new_list:[5], value:9. new_list:[5,10], value:2. new_list:[5,10,3], value:1. new_list:[5,10,3,2], value:none.
    return new_list

result = increment_all([4,9,2,1])