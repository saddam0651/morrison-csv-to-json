# File generator

The file generator tech test comes with a mock data CSV that represents one of the many types of data that we have to deal with at Morrisons.

The challenge is to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

## Getting Started

Use this repository as a starting point with the CSV file readily available in the root.

### Prerequisites

Use any IDE or resources that you would like. We would prefer that you attempt this challenge using Python.

## The desired form

From the CSV, you will see that the data follows a parent child structure. The first entry is always at the top of the tree, with the following entries being children of the previous column. The example below shows the structure that we would like to see.

```
[
  {
    "label": "Meat & Fish",
    "id": "179549",
    "link": "https://groceries.morrisons.com/browse/179549",
    "children": [
      {
        "label": "3 For £9.00 Meat & Poultry",
        "id": "179545",
        "link": "https://groceries.morrisons.com/browse/179549/179545",
        "children": []
      },
      {
        "label": "Fish",
        "id": "176741",
        "link": "https://groceries.morrisons.com/browse/179549/176741",
        "children": [
          {
            "label": "Fish Counter",
            "id": "176780",
            "link": "https://groceries.morrisons.com/browse/179549/176741/176780",
            "children": [
              {
                "label": "Salmon",
                "id": "176979",
                "link": "https://groceries.morrisons.com/browse/179549/176741/176780/176979",
                "children": []
              },
            ]
          }
        ]
      }
    ]
  }
]

```

## Deliverables

Replace the contents of this README.md with:

A covering note explaining the technology choices you have made.

1. Any instructions required to run your solution and tests in a Linux environment.
2. Email as an attachment or a link the git bundled repository showing your commit history with all your commits on the master branch:

```
    git bundle create <anything>.bundle --all
```
