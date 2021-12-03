
import statistics
from statistics import mode
import re

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

# print(final_len_depth(data2))

def final_pos(l,d):
    return l * d

# print(final_pos(1911,724))

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

def track_aim(lst):
    l = 0
    d = 0
    a = 0
    for line in data2:
        if line[0] == "f":
            l+= int(line[-2])
            d+= (a * int(line[-2]))
        
        if line[0] == "u":
            a -= int(line[-2])

        if line[0] == "d":
            a+= int(line[-2])
    return l, d, a
    
# print(track_aim(data2))
# print(final_pos(1911, 778813))

with open("./input3.csv", 'r') as binaries:
    data3 = binaries.readlines()
def calc_gamma_ep(lst):
    final_gamma = []
    final_ep = []
    pos1 = []
    pos2 = []
    pos3 = []
    pos4 = []
    pos5 = []
    pos6 = []
    pos7 = []
    pos8 = []
    pos9 = []
    pos10 = []
    pos11 = []
    pos12 = []
   
    for line in data3:
        pos1.append(line[0])
        pos2.append(line[1])
        pos3.append(line[2])
        pos4.append(line[3])
        pos5.append(line[4])
        pos6.append(line[5])
        pos7.append(line[6])
        pos8.append(line[7])
        pos9.append(line[8])
        pos10.append(line[9])
        pos11.append(line[10])
        pos12.append(line[11])
    final_gamma.append(mode(pos1))
    final_gamma.append(mode(pos2))
    final_gamma.append(mode(pos3))
    final_gamma.append(mode(pos4))
    final_gamma.append(mode(pos5))
    final_gamma.append(mode(pos6))
    final_gamma.append(mode(pos7))
    final_gamma.append(mode(pos8))
    final_gamma.append(mode(pos9))
    final_gamma.append(mode(pos10))
    final_gamma.append(mode(pos11))
    final_gamma.append(mode(pos12))

    for num in final_gamma:
        if num == "0":
            final_ep.append(1)
        if num == "1":
            final_ep.append(0)
    
    return final_gamma, final_ep

print(calc_gamma_ep(data3))
final_gamma = calc_gamma_ep(data3)[0]
#1508
#2587 => 3901196
# 010111100100
def find_closest(search_string, dta):
    #get the index of the biggest i and get the corresponding value in the dta
    closeness_lst = []
    for line in dta:
        for i in range(12):
            if search_string[:i] != line[:i]:
                closeness_lst.append(i)
    search_closest = max(closeness_lst)
    # print(search_closest)
    #i want the index of where the max is in my closest list and then i can get the value from my dta

    for i in range(len(closeness_lst)):
        if closeness_lst[i] == search_closest:
            final_index = i
            return dta[i]


# If 0 and 1 are equally common, keep values with a 1 in the position being considered.
print("all options for the ox rating:")
print(find_closest("010111100100", data3))
print(find_closest("110111100100", data3))

print("all options for the co2 rating:")
print(find_closest("101000011011", data3))
print(find_closest("001000011011", data3))
print(find_closest("000000011011", data3))

ox = [94, 163]
co2 = [163, 3748, 1639]

def calc(l1, l2):
    results = []
    for num in l1:
        for num2 in l2:
            results.append(num*num2)
    return results
print(calc(ox, co2))
#[15322, 352312, 154066, 26569, 610924]









# 11
# 000001011110 = 94

# 11
# 000010100011 = 163
