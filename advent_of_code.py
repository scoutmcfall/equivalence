
with open("./input.csv", 'r') as depths:
    data = depths.readlines()


def count_increase(lst):
    trip_list = []
    triple = zip(data, data[1:], data[2:])
    for first, second, third in triple:
        
        trip_list.append(sum([int(first), int(second), int(third)]))
    return trip_list    

def count_triple(lst):
    pairs = zip(lst, lst[1:])
    count = 0    
    for first, second in pairs:
        if int(second) > int(first):
            count+=1
    return count
trip_lst = count_increase(data)
# print(count_triple(trip_lst))

with open("./input2.csv", 'r') as directions:
    data2 = directions.readlines()

# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.

def final_len_depth(lst):
    l = 0
    d = 0
    for line in data2:
        if line[0] == "f":
            l+= int(line[-2])
        if line[0] == "u":
            d-= int(line[-2])
        if line[0] == "d":
            d+= int(line[-2])
    return l, d

print(final_len_depth(data))

def final_pos(l,d):
    return l * d

print(final_pos(1911,724))


