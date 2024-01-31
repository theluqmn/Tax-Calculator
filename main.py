from scripts import load, tools
import time

tools.Clear()
# Loading all the brackets
list = load.find_brackets()
for item in list:
    details = load.open_bracket(item)
    name = details["name"]
    country = details["country"]
    print(f"ID: {item} || Bracket: {name} | country: {country} | tiers: {len(details['tiers'])}")

bracket = input("Enter ID of bracket")

time.sleep(5)

tools.Clear()
tax = 0
salary = int(input("Enter your salary (yearly): "))
carry = salary #For calculatiosn above bracket 1

if salary > 0:
    for i in tax_bracket["tiers"]:
        tax_tier = i["tier"]
        tax_rate = i["rate"]
        tax_min = i["min"] / 100
        tax_max = i["max"] / 100
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