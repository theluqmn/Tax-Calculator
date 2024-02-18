# Tax Calculator

This is a basic tax calculator designed for countries with progressive taxation (aka, taxes with brackets).

The USA bracket and several copies (for testing) is included by default, in the `/tax_brackets` folder.

## How it works

First, this script lists down all available tax brackets. You will enter an ID for the tax bracket you would
like to use for the calculation (eg: USA.json).

Second, you will be instructed to input your **yearly** salary.

Lastly, it will begin to calculate your tax. It loops through the different tax brackets until
it locates the bracket that is within range of your salary. Once it successfully locates your bracket,
it will output your total tax and what tier you belong in, and will mention the tier's salary range.

Do note that this script is designed to have robust error-catching, whenever needed - such as checking
for missing files/folders. This project is part of Project ChainLink, as an exercise for robust, scalable
and redundant software solutions. This is also the first actual working project I made this year, ever
since my absence - which lasted roughly four months.

**Code written 100% by Luqman Yazrie (MY)**.
Special thanks to Hannah (US) for inspiring this project idea :D

## Tax Bracket JSON Format

Currently, this code follows the version 1 format. It consists of a version, name, country and updated year key, followed
by a list containing the tiers (each tier is a dictionary of its own).

Each different bracket follows a JSON format that can be read by this code, and it is as follow:

```json

{
    "format_version":1,
    "name": "US tax bracket (single-filers)",
    "country": "USA",
    "updated": 2021,
    "tiers": [
        {
            "tier":1,
            "rate":10,
            "min":0,
            "max":9875
        },
        {
            "tier":2,
            "rate":12,
            "min":9876,
            "max":40125
        },
    ]
}
```

You can add as much tiers as needed, according to your local tax laws. Each bracket is identified in the system through
the file name (eg: USA.json) as the ID.

Do note that the rate is in percentages (eg: 22 is 0.22x).

## Error Catching

`/tax_brackets` and `/scripts`, including all of its contents, is required for this tool to function.
`/tax_brackets` folder can be empty, and is checked for so when loading brackets. This will end up
in the tool informing you of so and exiting. Other error catching is just basic things, hence not worth
mentioning.

This script also checks if each of the individual tax brackets contains required keys, and follows the format that this code
is able to read. Refer to **Tax Bracket JSON Format** above for more information.
