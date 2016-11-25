import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False)
	email = Column(String(250), nullable  = False)
	picture = Column(String(250))


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	#creator = Column(String(80), nullable = False)

	@property
	def serialize(self):
		return {
		'name' : self.name,
		'id' : self.id,
		}

class Advice(Base):
	__tablename__ = 'advice'

	id = Column(Integer, primary_key = True)
	title = Column(String(80), nullable = False)
	body = Column(String(250), nullable = False)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)

	@property
	def serialize(self):
		return {
		'title':self.title,
		'body':self.body,
		'id':self.id,
		}

engine = create_engine('sqlite:///categoryadvice.db')

Base.metadata.create_all(engine)