from app import db, Countries, Cities
db.drop_all()
db.create_all()

UK = Countries(name='UK')
db.session.add(UK)
db.session.commit()

ldn=Cities(name='London', country=UK)
mcr=Cities(name='Manchester', country=Countries.query.filter_by(name='UK').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()
