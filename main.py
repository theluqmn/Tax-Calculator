from scripts import load, tools
import time, json

#Essential variables
tax = 0
bracket = None
config = {}
with open("config.json") as json_file:
    config = json.load(json_file)

#Bracket Selection
while True:
    tools.Clear()
    print("TAX BRACKETS FOUND IN FOLDER:\n")
    # Loading all the brackets
    list = load.find_brackets()
    for item in list:
        details = load.open_bracket(item)
        name = details["name"]
        country = details["country"]
        version = details["standard-version"]
        print(f"ID: {item}")
        print(f"Bracket: {name} | Country: {country} | Tiers: {len(details['tiers'])}\n")

        if version != config["standard-version"]:
            print(f"[!] THIS BRACKET IS NOT ON THE SAME FORMAT VERSION. Current format version is {config['standard-version']}")

    #Select an ID
    selection = input("> Enter ID of bracket for calculation: ")

    if selection in list:
        bracket = load.open_bracket(selection)
        break
    else:
        print(f"{selection} does not exist!")

tools.Clear()
print(f"Proceeding with {bracket['name']}\n")
salary = int(input("> Enter your salary (yearly): "))
carry = salary #For calculatiosn above bracket 1

# Tax calculation
if salary > 0:
    for i in bracket["tiers"]:
        tax_tier = i["tier"]
        tax_rate = i["rate"] / 100
        tax_min = i["min"]
        tax_max = i["max"]
        if salary >= tax_min and salary < tax_max:
            tax = carry * i["rate"]
            print(f"You are in TIER {tax_tier}. Total tax due: {tax} (includes all previous tiers)")
            break
        else:
            due = tax_max * tax_rate
            carry -= tax_max
            tax += due
            print(f"TIER {tax_tier}, {due} paid with rate {tax_rate}x and {carry} is left to calculate.\n")
else:
    print("lmao you're broke")