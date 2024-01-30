import modules

clear()
tax = 0
married = input("Are you married? (y/n): ").lower()
salary = int(input("Enter your salary (yearly): "))
carry = salary #For calculatiosn above bracket 1

if married == "y":
    pass
else:
    if salary > 0:
        for i in tax_bracket["single"]:
            if salary >= i["min"] and salary < i["max"]:
                tax = salary * i["rate"]
                print(f"You belong in bracket {i['tier']}. Total tax due: {tax}")
            else:
                due = i["max"] * i["rate"]
                carry -= i["max"]
                tax += due
                print(f"You're not in bracket {i['tier']}, {due} is paid in this bracket according to rate and {carry} is left for next bracket calculation.")
    else:
        print("lmao you're broke")