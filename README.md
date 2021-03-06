# File generator

The file generator tech test comes with a mock data CSV that represents one of the many types of data that we have to deal with at Morrisons.

The challenge is to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

## Input File

CSV File

### Output File

JSON File 

## Program File

Language: Python 3

Imports: csv, json

It takes the input file located in base directory and converts into hierarchical order of any length upto a level of 10 of any number of rows.

It returns a JSON file in the base directory.

Output achieved is displayed below.

```
{
    "label": "THE BEST",
    "id": "178974",
    "url": "https://groceries.morrisons.com/browse/178974",
    "child": [
        {
            "label": "FRESH",
            "id": "178969",
            "url": "https://groceries.morrisons.com/browse/178974/178969",
            "child": [
                {
                    "label": "CHEESE",
                    "id": "178975",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178975",
                    "child": []
                },
                {
                    "label": "COOKED MEAT & ANTIPASTI",
                    "id": "178976",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178976",
                    "child": []
                },
                {
                    "label": "DAIRY & EGGS",
                    "id": "178977",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178977",
                    "child": []
                },
                {
                    "label": "DESSERTS",
                    "id": "178978",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178978",
                    "child": []
                },
                {
                    "label": "DRINKS",
                    "id": "178979",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178979",
                    "child": []
                },
                {
                    "label": "FISH & SEAFOOD",
                    "id": "178980",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178980",
                    "child": []
                },
                {
                    "label": "FRUIT & VEGETABLES",
                    "id": "178981",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178981",
                    "child": []
                },
                {
                    "label": "MEAT & POULTRY",
                    "id": "178982",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178982",
                    "child": []
                },
                {
                    "label": "NUTS & SNACKS",
                    "id": "178983",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178983",
                    "child": []
                },
                {
                    "label": "PIES & QUICHES ",
                    "id": "178984",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178984",
                    "child": []
                },
                {
                    "label": "PIZZA, PASTA & GARLIC BREAD",
                    "id": "178985",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178985",
                    "child": []
                },
                {
                    "label": "READY MEALS",
                    "id": "178986",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178986",
                    "child": []
                },
                {
                    "label": "SAVOURY SNACKS & CHILLED",
                    "id": "178987",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178987",
                    "child": []
                },
                {
                    "label": "SOUPS & SAUCES",
                    "id": "178988",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178988",
                    "child": []
                },
                {
                    "label": "VEGETARIAN",
                    "id": "178989",
                    "url": "https://groceries.morrisons.com/browse/178974/178969/178989",
                    "child": []
                }
            ]
        },
        {
            "label": "FOOD CUPBOARD",
            "id": "178970",
            "url": "https://groceries.morrisons.com/browse/178974/178970",
            "child": [
                {
                    "label": "ANTIPASTI",
                    "id": "178990",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178990",
                    "child": []
                },
                {
                    "label": "BISCUITS & CRACKERS",
                    "id": "178991",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178991",
                    "child": []
                },
                {
                    "label": "BREAKFAST CEREALS",
                    "id": "178992",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178992",
                    "child": []
                },
                {
                    "label": "CHOCOLATE & SWEETS",
                    "id": "178993",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178993",
                    "child": []
                },
                {
                    "label": "CONDIMENTS & DRESSINGS",
                    "id": "178994",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178994",
                    "child": []
                },
                {
                    "label": "CRISPS & SAVOURY SNACKS",
                    "id": "178995",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/178995",
                    "child": []
                },
                {
                    "label": "HOMEBAKING",
                    "id": "179016",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179016",
                    "child": []
                },
                {
                    "label": "JAMS, SPREADS & CHUTNEYS",
                    "id": "179017",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179017",
                    "child": []
                },
                {
                    "label": "PASTA",
                    "id": "179018",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179018",
                    "child": []
                },
                {
                    "label": "PUDDINGS & DESSERTS",
                    "id": "179019",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179019",
                    "child": []
                },
                {
                    "label": "SAUCES, STOCKS & GRAVY",
                    "id": "179020",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179020",
                    "child": []
                },
                {
                    "label": "TEA & COFFEE",
                    "id": "179021",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179021",
                    "child": []
                },
                {
                    "label": "TINS & CANS",
                    "id": "179022",
                    "url": "https://groceries.morrisons.com/browse/178974/178970/179022",
                    "child": []
                }
            ]
        },
        {
            "label": "BAKERY & CAKES",
            "id": "178971",
            "url": "https://groceries.morrisons.com/browse/178974/178971",
            "child": [
                {
                    "label": "BREAD & BREAD ROLLS",
                    "id": "179023",
                    "url": "https://groceries.morrisons.com/browse/178974/178971/179023",
                    "child": []
                },
                {
                    "label": "CAKES, PIES & TARTS",
                    "id": "179024",
                    "url": "https://groceries.morrisons.com/browse/178974/178971/179024",
                    "child": []
                },
                {
                    "label": "CROISSANTS & BREAKFAST BAKERY",
                    "id": "179025",
                    "url": "https://groceries.morrisons.com/browse/178974/178971/179025",
                    "child": []
                },
                {
                    "label": "DESSERTS & PUDDINGS",
                    "id": "179026",
                    "url": "https://groceries.morrisons.com/browse/178974/178971/179026",
                    "child": []
                },
                {
                    "label": "FRUITED BREAD, SCONES & HOT CROSS BUNS",
                    "id": "179027",
                    "url": "https://groceries.morrisons.com/browse/178974/178971/179027",
                    "child": []
                }
            ]
        },
        {
            "label": "FROZEN",
            "id": "178972",
            "url": "https://groceries.morrisons.com/browse/178974/178972",
            "child": [
                {
                    "label": "CAKES, PIES & TARTS",
                    "id": "179028",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179028",
                    "child": []
                },
                {
                    "label": "CHIPS, POTATOES & VEGETABLES",
                    "id": "179029",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179029",
                    "child": []
                },
                {
                    "label": "DESSERTS",
                    "id": "179030",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179030",
                    "child": []
                },
                {
                    "label": "FISH & SEAFOOD",
                    "id": "179031",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179031",
                    "child": []
                },
                {
                    "label": "ICE CREAM & LOLLIES",
                    "id": "179032",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179032",
                    "child": []
                },
                {
                    "label": "MEAT & POULTRY",
                    "id": "179033",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179033",
                    "child": []
                },
                {
                    "label": "PIES & PASTRIES",
                    "id": "179034",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179034",
                    "child": []
                },
                {
                    "label": "PIZZA & GARLIC BREAD",
                    "id": "179035",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179035",
                    "child": []
                },
                {
                    "label": "READY MEALS",
                    "id": "179036",
                    "url": "https://groceries.morrisons.com/browse/178974/178972/179036",
                    "child": []
                }
            ]
        },
        {
            "label": "DRINKS",
            "id": "178973",
            "url": "https://groceries.morrisons.com/browse/178974/178973",
            "child": [
                {
                    "label": "SOFT DRINKS",
                    "id": "179037",
                    "url": "https://groceries.morrisons.com/browse/178974/178973/179037",
                    "child": []
                },
                {
                    "label": "WINE & SPARKLING",
                    "id": "179038",
                    "url": "https://groceries.morrisons.com/browse/178974/178973/179038",
                    "child": []
                },
                {
                    "label": "BEER",
                    "id": "179039",
                    "url": "https://groceries.morrisons.com/browse/178974/178973/179039",
                    "child": []
                }
            ]
        }
    ]
}
```
