# import requests
# res = requests.get("https://adventofcode.com/2021/day/1/input")
with open("./input.csv", 'r') as depths:
    data = depths.readlines()

# depths = []
# #looping through the iterator:
# for num in data:
#   depths.append(num)
# print(depths)

# def count_increase(lst):
#     count = 0
#     for i in range(len(lst)-1):
#         if lst[i+1] > lst[i]:
#             count+=1
#     return(count)

def count_increase(lst):
    count = 0
    pairs = zip(data, data[1:])
    for first, second in pairs:
        if int(second) > int(first):
            count+=1
    return count
print(count_increase(data))

# test=[199,200,208,210, 200, 207, 240, 269, 260, 263]
# print(count_increase(test))

