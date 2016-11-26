from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Category, Advice, User


engine = create_engine('sqlite:///categoryadviceuser.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

User1 = User(name = "Munkh1", email="munkhxxw@gmail.com", picture = "https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")

session.add(User1)
session.commit()

category1 = Category(name = "KosenSeigatsu", user  = User1)
session.add(category1)
session.commit()

advice1 = Advice(title = "Blah", body = "Ingeh yostoi", category = category1, user  = User1)
session.add(advice1)
session.commit()

advice2 = Advice(title = "Blah2", body = "Tegeh yostoi", category = category1, user  = User1)
session.add(advice2)
session.commit()

advice3 = Advice(title = "Blah3", body = "Herheh yostoi", category = category1, user  = User1)
session.add(advice3)
session.commit()

advice4 = Advice(title = "Blah4", body = "Zaah yostoi", category = category1, user  = User1)
session.add(advice4)
session.commit()

User2 = User(name = "Munkh2", email="munkhwwx@gmail.com", picture = "https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")

session.add(User2)
session.commit()

category2 = Category(name = "Hennyuu", user  = User2)
session.add(category2)
session.commit()

advice1 = Advice(title = "Blah", body = "Ingeh yostoi", category = category2, user  = User2)
session.add(advice1)
session.commit()

advice2 = Advice(title = "Blah2", body = "Tegeh yostoi", category = category2, user  = User2)
session.add(advice2)
session.commit()

advice3 = Advice(title = "Blah3", body = "Herheh yostoi", category = category2, user  = User2)
session.add(advice3)
session.commit()

advice4 = Advice(title = "Blah4", body = "Zaah yostoi", category = category2, user  = User2)
session.add(advice4)
session.commit()

print "added menu items!"