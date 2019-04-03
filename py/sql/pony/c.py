import json
from itertools import groupby
from operator import itemgetter
from pprint import pprint as pp

get = lambda x: itemgetter(x)

rows = []
with open('c.json') as f:
	rows = json.loads(f.read())

pp(rows[0])

keys = ['field_code', 'display', 'data_set_id']
from datetime import datetime
for x in rows:
	if x['type'] == 'datetime':
		y = datetime.strptime(x['value'], '%d-%m-%Y')
		x['value'] = y

pp(map(get('value'), rows), indent=2)

# print(list(groupby(rows, itemgetter('field_id'))))