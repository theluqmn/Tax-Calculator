import os, json

folder = os.listdir('./tax_brackets')

def find_brackets():
    tax_brackets = []

    #List down all tax brackets in folder
    for file in folder:
        if file.endswith(".json"):
            tax_brackets.append(file)

    return tax_brackets

def lookup_bracket(file):
    with open(f"{os.getcwd}/./")