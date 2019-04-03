from datetime import datetime
from app import db, Cat, User

# db.create_all()

# db.session.add(Cat(name="Meowington"))
# db.session.add(Cat(name="Snuggles"))
# db.session.add(Cat(name="Wiggles"))
# db.session.add(Cat(name="Sheriff"))
# db.session.add(User(username="admin", email="admin@ex.com"))
# db.session.add(User(username='guest', email='guest@ex.com'))

db.session.commit()
for x in User.query.all():
	print(x)
for x in Cat.query.all():
	print('*', x.name)


# class Post(db.Model):
# 	id = db.Column()