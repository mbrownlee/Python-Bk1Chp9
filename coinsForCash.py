    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `total_dollars` and print it.
def calc_dollars(**coins):

    total_dollars = 0
    for coin, amount in coins.items():
        if coin == "pennies": 
            total_dollars += amount * .01
        elif coin == "nickels":
            total_dollars += amount * .05
        elif coin == "dimes":
            total_dollars += amount * .1
        elif coin == "quarters":
            total_dollars += amount * .25
    print(total_dollars)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
calc_dollars(pennies= 578, nickels=934, dimes=732, quarters=475)