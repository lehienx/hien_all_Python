from tinydb import TinyDB, Query

filepath = "database/TinyDB.json"
db = TinyDB(filepath)

db.purge_table('fruits')
table = db.table('fruits')
table.insert({'name': 'Banana', 'price': 900})
table.insert({'name': 'Orange', 'price': 900})
table.insert({'name': 'Mango', 'price': 600})

print(table.all())

item = Query()
res = table.search(item.name == 'Orange')
print('orange is ', res[0]['price'])
print('more 800 :')
res = table.search(item.price >= 800)
for it in res:
    print('-', it['name'])
