from scripts import clear
import json

tax_bracket = None #Loading tax bracket json
with open("tax_bracket.json") as json_file:
    tax_bracket = json.load(json_file)

clear.Clear()
tax = 0
married = input("Are you married? (y/n): ").lower() #Doesnt matter at the moment
salary = int(input("Enter your salary (yearly): "))
carry = salary #For calculatiosn above bracket 1

if salary > 0:
    for i in tax_bracket["single"]:
        tax_tier = i["tier"]
        tax_rate = i["rate"]
        tax_min = i["min"]
        tax_max = i["max"]
        if salary >= tax_min and salary < tax_max:
            tax = carry * i["rate"]
            print(f"You belong in bracket {tax_tier}. Total tax due: {tax}")
            break
        else:
            due = tax_max * tax_rate
            carry -= i["max"]
            tax += due
            print(f"You're not in bracket {i['tier']}, {due} is paid in this bracket according to rate and {carry} is left for next bracket calculation.")
else:
    print("lmao you're broke")