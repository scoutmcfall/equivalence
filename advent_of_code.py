import numpy as np
import statistics
from statistics import mode, median
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
    #could sort the lists and then take the middle value
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
#4412188

with open("./input5.csv", 'r') as bingo:
    data4 = bingo.read() #reads it into a string

#which board will win first and what is the score of that board?

def bingo0(DATA):
    #split all the input data by double space
    data = DATA.strip().split('\n\n')
    #isolate the called bingo numbers at the beginning
    sequence = map(int, data[0].split(","))
    #make each line in each board a list
    boards_ar = np.array([[list(map(int,line.split())) for line in board.split("\n")] for board in data[1:] if board])
    #transpost the columns in each board into lists
    t_boards_ar = np.array(list(map(lambda x: x.T, boards_ar)))
    boards = boards_ar.tolist()+t_boards_ar.tolist()
    print(boards)
    #iterate through each num in the sequence, removing the number from the row list
    for num in sequence:
        for board in boards:
            for row in board:
                if num in row:
                    row.remove(num)
            #if the board is missing any values (they've been called, return the sum for the board)
            #print(board)
            if not all(board):
                print(board)
                return sum([x for row in board for x in row])*num

#print(bingo(data4))

with open('./input4.csv') as file:
    lines = [line.rstrip() for line in file.readlines()]
n = [28,82,77,88,95,55,62,21,99,14,30,9,97,92,94,3,60,22,18,86,78,71,61,43,79,33,65,81,26,49,47,51,0,89,57,75,42,35,80,1,46,83,39,53,40,36,54,70,76,38,50,23,67,2,20,87,37,66,84,24,98,4,7,12,44,10,29,5,48,59,32,41,90,17,56,85,96,93,27,74,45,25,15,6,69,16,19,8,31,13,64,63,34,73,58,91,11,68,72,52]

class Bingo():
    def __init__(self, board):
        self.board = [x.split() for x in board]

    def mark(self, n):
        for row in self.board:
            for i, item in enumerate(row): 
                if item == n:
                    row[i] = 'X'

    def has_won(self):
        for x in range(len(self.board)):
            col, row = 0, 0
            for y in range(len(self.board)):
                col += int(self.board[y][x] == 'X')
                row += int(self.board[x][y] == 'X')
            if col == 5 or row == 5: 
                return True
        return False

    def get_score(self):
        score = 0 
        for row in self.board: 
            for item in row: 
                score += int(item) if item != 'X' else 0
        return score


#day 5:
d = [[int(x) for x in l.replace(" -> "," ").replace(","," ").split()] for l in open("./input5.csv","rt")]
a = {}
b = {}
for x1,y1,x2,y2 in d:
  if x1==x2:
    if y1>y2: y1,y2=y2,y1
    for y in range(y1,y2+1):
      a[(x1,y)]=a.get((x1,y),0)+1
      b[(x1,y)]=b.get((x1,y),0)+1
  elif y1==y2:
    if x1>x2: x1,x2=x2,x1
    for x in range(x1,x2+1):
      a[(x,y1)]=a.get((x,y1),0)+1
      b[(x,y1)]=b.get((x,y1),0)+1
  else:
    if x1>x2: x1,x2, y1,y2 = x2,x1, y2,y1
    for x in range(x1,x2+1):
      if y2>y1: y = y1+(x-x1)
      else:     y = y1-(x-x1)
      b[(x,y)]=b.get((x,y),0)+1
print( sum(v>1 for v in a.values()) )
print( sum(v>1 for v in b.values()) )


#day 6:
with open("./input6.csv") as file:
    ages = [int(x) for x in file.read().split(",")]


def simulate(fish_ages):
    count = [fish_ages.count(i) for i in range(9)]
    result_at_day_80 = 0
    for day in range(1, 256+1):
        zeros = count[0]
        count[:-1] = count[1:]
        count[6] += zeros
        count[8] = zeros
        if day == 80:
            result_at_day_80 = sum(count)
    return result_at_day_80, sum(count)

#day 7:
with open("./input7.csv") as file:
    positions =  [int(x) for x in file.read().split(",")]
print("**********************")
print(median(positions))
print(mode(positions))
def least_fuel(x_positions):
    fuel_cnt = 0
    for num in x_positions:
        fuel_cnt += abs(num - 330)
    return fuel_cnt
#in my case it was just the median value that was the most efficient?

print(least_fuel(positions))


