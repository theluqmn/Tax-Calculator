from scripts import load, tools
import time

#Essential variables
tax = 0
bracket = None

#Bracket Selection
while True:
    tools.Clear()
    # Loading all the brackets
    list = load.find_brackets()
    for item in list:
        details = load.open_bracket(item)
        name = details["name"]
        country = details["country"]
        print(f"ID: {item} || Bracket: {name} | Country: {country} | Tiers: {len(details['tiers'])}\n")

    #Select an ID
    selection = input("Enter ID of bracket: ")

    if selection in list:
        bracket = load.open_bracket(selection)
        break
    else:
        print(f"{selection} does not exist!")

tools.Clear()
print(f"Proceeding with {bracket['name']}")
salary = int(input("Enter your salary (yearly): "))
carry = salary #For calculatiosn above bracket 1

if salary > 0:
    for i in bracket["tiers"]:
        tax_tier = i["tier"]
        tax_rate = i["rate"] / 100
        tax_min = i["min"]
        tax_max = i["max"]
        if salary >= tax_min and salary < tax_max:
            tax = carry * i["rate"]
            print(f"You belong in bracket {tax_tier}. Total tax due: {tax}")
            break
        else:
            due = tax_max * tax_rate
            carry -= tax_max
            tax += due
            print(f"You're not in bracket {tax_tier}, {due} is paid in this bracket according to rate and {carry} is left for next bracket calculation.")
else:
    print("lmao you're broke")