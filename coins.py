
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
    result_set = set()
    max_dimes = goal_cents//10
    max_nickles = goal_cents//5

    print(max_dimes)
    for i in range(max_dimes + 1):
        dime_amt = ((max_dimes -i)*10)
        dime_cnt = (dime_amt/10)
        penny_cnt = ((goal_cents - dime_amt)%5)
        nickle_cnt = ((goal_cents - dime_amt - penny_cnt)/5)
        mix = f"{dime_cnt}/{nickle_cnt}/{penny_cnt}"
        result_set.add(mix)
    print(result_set)
    for i in range(max_nickles + 1):
        nickle_amt = ((max_nickles -i)*5)
        nickle_cnt = (nickle_amt/5)
        penny_cnt = ((goal_cents - nickle_amt)%10)
        dime_cnt = ((goal_cents - nickle_amt - penny_cnt)/10)
        mix = f"{dime_cnt}/{nickle_cnt}/{penny_cnt}"
        result_set.add(mix)
    print(result_set)




# def mixed_calc(goal_cents):


small_calc(32)
total_calc(32)