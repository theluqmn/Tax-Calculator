'''
Tax Calculator.
Made by Luqman Yazrie (MY), using Python 3.11 64-bit.
https://github.com/luqmanity
'''

import json, os

#Safety checks
if "config.json" and "tax_brackets" and "scripts" not in os.listdir(): #Check if there is any missing files
    print("Missing files, visit https://github.com/luqmanity/taxed for source code.")

else: #Checking for missing essential scripts
    if "load.py" and "tools.py" not in os.listdir("./scripts"): #Checks if any scripts are missing:
        print("Missing essential scripts in the /script folder.")
    
    else: #Cleared to proceed
        from scripts import load, tools

        #Essential variables
        tax = 0
        bracket = None
        config = {}
        with open("config.json") as json_file: #Checking for config.json
            config = json.load(json_file)

        #Bracket Selection
        while True:
            tools.Clear()
            print("TAX BRACKETS FOUND IN FOLDER:\n")
            # Loading all the brackets
            list = load.find_brackets()

            if list == None: #If no tax brackets in folder
                print("No tax brackets found in folder. Note that tax brackets belong in the /tax_brackets folder.")
                break

            for item in list: #Looping in all available tax brackets
                details = load.open_bracket(item)
                try: #Loads the parameters
                    name = details["name"]
                    country = details["country"]
                    version = details["format_version"]

                    print(f"ID: {item}")
                    print(f"Bracket: {name} | Country: {country} | Tiers: {len(details['tiers'])}\n")

                    if version != config["format_version"]: #Checks if the JSON's format version is the similar as this code's
                        print(f"[!] THIS BRACKET IS NOT ON THE SAME FORMAT VERSION. Current format version is {config['format_version']}")

                except: #Catches error if keys are missing/does not follow format
                    print(f"{item} DOES NOT HAVE REQUIRED PARAMETERS, AND MAY NOT FOLLOW THE FORMAT VERSION {config['format_version']}.")

            #Select an ID
            selection = input("> Enter ID of bracket for calculation: ")

            if selection in list: #Checking if ID input is in available brackets
                bracket = load.open_bracket(selection)
                break

            else:
                print(f"{selection} does not exist!")

        #Begin calculation
        tools.Clear()
        print(f"Proceeding with {bracket['name']}\n")
        salary = int(input("> Enter your salary (yearly): "))
        carry = salary #For calculations above bracket 1

        # Tax calculation
        if salary > 0:
            for i in bracket["tiers"]: #Loops in all the listed tax brackets
                tax_tier = i["tier"]
                tax_rate = i["rate"] / 100 #Percentage to decimal conversion
                tax_min = i["min"]
                tax_max = i["max"]

                if salary >= tax_min and salary < tax_max: #Within tax tier i
                    tax = carry * tax_rate

                    print(f"You are in TIER {tax_tier}. Total tax due: {tax} (includes all previous tiers)\n")
                    break

                else: #Not within this tax tier
                    due = tax_max * tax_rate
                    tax += due
                    carry -= due

                    print(f"TIER {tax_tier}, {due} paid with rate {tax_rate}x and {carry} is left to calculate.\n")

        else: #BROKIE😂
            print("lmao you're broke XD")