import json
import csv

with open('../../data.csv') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)
    dict = {}
    count = -1
    len1 = 0
    len_bkp = len1
    level = 1
    for row in reader:
        if row[0]:
            items = [item for item in row if item]
            items.pop(0)
            len2 = len(items)

            if len1 == len2:
                len1 = len_bkp
                level -= 1

            if len1 > len2:
                len1 -= len_bkp
                len_bkp = len1
                level = 2

            items = items[len1:len2]

            if level == 1:
                dict = {'label': items[0], 'id': items[1], 'url': items[2], 'child': []}
            elif level == 2:
                dict['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 3:
                dict['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 4:
                dict['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 5:
                dict['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 6:
                dict['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 7:
                dict['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 8:
                dict['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 9:
                dict['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            elif level == 10:
                dict['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'][-1]['child'].append({'label': items[0], 'id': items[1], 'url': items[2], 'child': []})
            else:
                pass

            if len2 > len1:
                level += 1
                len_bkp = len1
                len1 = len2

with open ('../../morrisons-groceries.json', 'w') as f:
    json.dump(dict, f, indent=4)

