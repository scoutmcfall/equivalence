
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


# def total_calc(goal_cents):


# def mixed_calc(goal_cents):


small_calc(244)