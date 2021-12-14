# Enter your code here. Read input from STDIN. Print output to STDOUT
#result(first line): false if some rooms not guarded, true if all rooms guarded
#if false, return coordinates of unguarded rooms (ascending)
#museum is smaller than 100x100
#input first line: dimensions (l*w)
import sys
data = sys.stdin.readlines()
dimensions = data[0].split()

museum = []
for i in range(int(dimensions[1])):
    row = []
    for j in range(int(dimensions[0])):
        row.append(0)
    museum.append(row)

columns = []
for i in range(int(dimensions[0])):
    row = []
    for j in range(int(dimensions[1])):
        row.append(0)
    columns.append(row)
    
data.pop(0)#get rid of dimensions
unguarded_rooms = []
for line in data:#iterate through each line in data, replacing the 0s
#in my rows with the w or g vals
    coordinates = line.split(" ")
    museum[int(coordinates[1])][int(coordinates[0])] = coordinates[2]
    columns[int(coordinates[0])][int(coordinates[1])] = coordinates[2]

guarded_room_count = 0
print ("**************************")
#a problem with using .index is it only returns the first occurrence, so what if there's multiple g and ws in each row?
for row in museum:
    if "g\n" in row:
        column = columns[row.index("g\n")] #check this intersecting column
        #whatever the distance is between the g and the w in the row/column is what i'll add to my count
        if "w\n" in row:
             #mark unguarded rooms with 1
            if row.index("g\n")< row.index("w\n"): #i want to mark the unguarded rooms with 1 but it's not reaching
                guarded_room_count += (row.index("w\n")-row.index("g\n"))
                # for room in row[row.index("g\n")+1:]:
                #     if room == 0:
                #         room = 1
                print(row)
            if row.index("w\n")< row.index("g\n"):
                guarded_room_count += (row.index("g\n")-row.index("w\n"))

                for room in row[:row.index("w\n")]:
                    print(room)
                    # if room == 0:
                    #     room = "1"
                print(row)
            if "w\n" in column:
                guarded_room_count += (column.index("g\n")-column.index("w\n"))
                
                #mark unguarded rooms with 1
                if column.index("g\n")< column.index("w\n"): 
                # for room in row[row.index("g\n")+1:]:
                #     if room == 0:
                #         room = 1
                    print(column)
                if column.index("w\n")< column.index("g\n"):
                    for room in column[:column.index("w\n")]:
                        print(column)
                        # if room == 0:
                        #     room = "1"
                    print(column)
            guarded_room_count += len(column[column.index("g\n"):])
        
        else:
            guarded_room_count += len(row[row.index("g\n"):])
            guarded_room_count += len(column[column.index("g\n"):])

print("****************")
print(museum)

if guarded_room_count < (int(dimensions[0])*int(dimensions[1])):
    print("False")


            

# # use a stack and iterate through each line, adding to the room cnt between g and w
# for row in museum:
#     stack = []
#     for room in row:
#         if room == "g\n":
#             stack.append(room)
#             guarded_room_count +=1
#         if room == "w\n":
#             stack = []
#         if stack and stack[0] == "g\n":
#             guarded_room_count += 1
# print(guarded_room_count)
    
# #make a master list representing columns and do the same thing? how do i account for duplicates?

# for column in columns:
#     stack = []
#     for room in column:
#         if room == "g\n":
#             stack.append(room)
#             guarded_room_count +=1
#         if room == "w\n":
#             stack = []
#         if stack and stack[0] == "g\n":
#             guarded_room_count += 1
#     # guarded_room_count += len(stack)
# print(guarded_room_count)



"""instructions:
1h 49m left

Skip to main content
ALL
1
1. Museum Security
This exercise will be open for 6 hours, although it shouldn't take more than 2. Please note, the test will cut off after 6 hours. 

 

Suppose you've been asked to verify a museum's security is up to standard.

 

You're given a floor plan with the positions of all guards and walls:

 

4 6
0 0 g
0 1 w
1 1 g
2 2 w
2 3 g
 

The first line describes the dimensions of the museum, which is a m x n
rectangle (in this case, 4 x 6). m and n are always greater than 0.

 

Subsequent lines correspond to positions of guards (designated as "g") and
walls (designated as "w"). For example, "0 0 g" designates there is a
guard at (0, 0).

 

Guards do not move, but can guard any line of rooms that are:

directly to the north, east, south, or west of them
unobstructed (i.e., there is no wall in between them)
 

For example, the guard at (0, 0) can only guard (1, 0), (2, 0), and (3, 0).

 

Whereas the guard at (2, 3) can guard (0, 3), (1, 3), (2, 4), (2, 5), and (3, 3).

 

The above museum looks something like:

 

 	0	1	2	3	4	5
0	g	w	 	-	 	 
1	-	g	-	-	-	-
2	-	-	w	g	-	-
3	-	-	 	-	 	 
 

Guarded rooms have been marked with a "-".

 

Given a museum, please print your solution in the following format:

 

false
0 2
0 4
0 5
3 2
3 4
3 5
 

The first line should be "false" if the museum has unguarded rooms, and "true"
if the museum has no unguarded rooms.

 

If "false", subsequent lines should be coordinates of unguarded rooms.


Unguarded rooms should be ordered in ascending order by (x, y).

 

Some quick notes:

For certain languages (e.g., Ruby) we've provided a helper method to load the museum. You do not need to use this method if don't want to.
You will always be provided valid inputs.
The museums will never be larger than 100 x 100.
While not required, we'd prefer a solution that runs in time O(m n)."""