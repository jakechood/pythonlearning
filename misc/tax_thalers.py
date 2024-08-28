income_amt = float(input("Enter the annual income: "))

'''(int) ->float"

    return the amount of taxes due,
    according to the annual income,
    based on thalers in imaginary world'''

if float(income_amt) < 85528.0:
    tax = income_amt * .18 - 556.2
elif float(income_amt) >= 85528.0:
    tax = ((income_amt - 85528)*.32) + 14839.2
elif tax < 0.0:
    tax = 0.0

tax = float(round(tax, 0))
print("The tax is:", tax, "thalers")
