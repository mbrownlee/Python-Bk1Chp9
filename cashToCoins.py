dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
def calc_coins(dollars):
    piggyBank["quarters"] += dollars // .25
    dollars = dollars % .25
    piggyBank["dimes"] += dollars // .1
    dollars = dollars % .1
    piggyBank["nickels"] += dollars // .05
    dollars = dollars % .05
    piggyBank["pennies"] += dollars // .01
    dollars = dollars % .01
# That should produce the following output.
calc_coins(dollarAmount)
print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }
# Double "//" made it happen without decimals. With single / had 34.9999 quareters instead of 34. Research taught me the // is a floor division and yields the quotient, not the remainder.