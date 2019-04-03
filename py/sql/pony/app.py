from pony.orm import *

db = Database()
db.bind(provider='mysql', host='', user='', passwd='', db='')

class Person(db.Entity):
	name = Required(str)
	age = Required(int)
	cars = Set('Car')

class Car(db.Entity):
	make = Required(str)
	model = Required(str)
	owner = Required(Person)

db.bind(
	provider='sqlite',
	filename='tutorial1.db',
	create_db=True
)

db.generate_mapping(create_tables=True)
# set_sql_debug(True)

with db_session:
	select(car for car in Car if car.owner == Person.get(name="Dinesh")).show()