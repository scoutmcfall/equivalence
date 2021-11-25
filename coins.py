
"""1. smallest number of coins (using pennies and dimes and nickles) to sum goal_cents
2. find total number of ways you can make the goal_cents
3. how many of those solutions have mixed dimes and nickles"""

def small_calc(goal_cents):
    n_p = (goal_cents % 10) #remainder that gets divided up between nickles and pennies
    
    pennies = (n_p % 5) #remainder that is pennies

    dimes = (goal_cents - pennies)//10

    nickles = (goal_cents - pennies - (dimes * 10))/5

    print(dimes, nickles, pennies)
    return (pennies + nickles + dimes)


def total_calc(goal_cents):
#return all possible ways of making goal cents
#my current way has 6 dupes, meaning 1 in 7 is unnecessary

    result_lst = []
    result_set = set()
    max_dimes = goal_cents//10
    max_nickles = goal_cents//5
    required_penny_min = (goal_cents%5)

    for i in range(max_dimes + 1):
        dime_amt = ((max_dimes -i)*10)
        dime_cnt = int(dime_amt/10)
        penny_cnt = ((goal_cents - dime_amt)%5)
        nickle_cnt = int((goal_cents - dime_amt - penny_cnt)/5)
        mix = f"{dime_cnt}/{nickle_cnt}/{penny_cnt}"
        result_set.add(mix)
        result_lst.append(mix)
    print(result_set)
    for i in range(max_nickles + 1):
        nickle_amt = ((max_nickles -i)*5)
        nickle_cnt = int(nickle_amt/5)
        penny_cnt = ((goal_cents - nickle_amt)%10)
        dime_cnt = int((goal_cents - nickle_amt - penny_cnt)/10)
        mix = f"{dime_cnt}/{nickle_cnt}/{penny_cnt}"
        result_set.add(mix)
        result_lst.append(mix)

    print(result_set)
    for i in range(required_penny_min, goal_cents):
        nickle_cnt = int(((goal_cents - i)%10)/5)
        penny_cnt = i
        dime_cnt = int(goal_cents - penny_cnt - (nickle_cnt*5))/10

        mix = f"{dime_cnt}/{nickle_cnt}/{penny_cnt}"
        result_set.add(mix)
        result_lst.append(mix)

    print(result_set)
    print(len(result_set))
    print(len(result_lst))
    return result_lst

def mixed_calc(result_lst):
    count = 0
    for result in result_lst:
        if int(result[0]) > 0 and int(result[2]) > 0 and int(result[-1]) == 0:
            count += 1
    print("*************************")
    print(count)
    return count


# small_calc(32)
result_lst = total_calc(107)
mixed_calc(result_lst)