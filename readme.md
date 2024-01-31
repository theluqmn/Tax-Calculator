# Tax Calculator
This is a basic tax calculator designed for countries with progressive taxation (aka, taxes woth brackets)

The USA bracket and several copies (for testing) is included by default, in the `/tax_brackets` folder.

## Tax Bracket JSON format
Currently, this code follows the version 1 format. It consists of a version, name, country and updated year key, followed
by a list containing the tiers (each tier is a dictionary of its own).

Do note that

Each different bracket follows a JSON format that can be read by this code, and it is as follow:
```
{
    "standard-version":1,
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
You can add as much tiers as needed.