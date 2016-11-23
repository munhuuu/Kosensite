from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Category, Advice


engine = create_engine('sqlite:///categoryadvice.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

category1 = Category(name = "KosenSeigatsu")
session.add(category1)
session.commit()

advice1 = Advice(title = "Blah", body = "Ingeh yostoi", category = category1)
session.add(advice1)
session.commit()

advice2 = Advice(title = "Blah2", body = "Tegeh yostoi", category = category1)
session.add(advice2)
session.commit()

advice3 = Advice(title = "Blah3", body = "Herheh yostoi", category = category1)
session.add(advice3)
session.commit()

advice4 = Advice(title = "Blah4", body = "Zaah yostoi", category = category1)
session.add(advice4)
session.commit()

category2 = Category(name = "Hennyuu")
session.add(category2)
session.commit()

advice1 = Advice(title = "Blah", body = "Ingeh yostoi", category = category2)
session.add(advice1)
session.commit()

advice2 = Advice(title = "Blah2", body = "Tegeh yostoi", category = category2)
session.add(advice2)
session.commit()

advice3 = Advice(title = "Blah3", body = "Herheh yostoi", category = category2)
session.add(advice3)
session.commit()

advice4 = Advice(title = "Blah4", body = "Zaah yostoi", category = category2)
session.add(advice4)
session.commit()

print "added menu items!"