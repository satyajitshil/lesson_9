unit = int(input("How many units did you use:"))

if unit < 50:
    ammount = 2.60 * unit
    subcharge = 25
elif 50 <= unit < 100:
    ammount = 3.25 * unit
    subcharge = 35
elif 100 <= unit <= 200:
    ammount = 5.26
    subcharge = 50
elif unit > 200:
    ammount = 8.45
    subcharge = 80

print(ammount + subcharge)