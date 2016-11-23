from flask import Flask, render_template, request, redirect, url_for,flash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Category, Advice


engine = create_engine('sqlite:///categoryadvice.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


app = Flask(__name__)

@app.route('/')
@app.route('/allcategories')
def allCategories():
	categories = session.query(Category).order_by(Category.name.asc()).all()
	return render_template('allCategories.html', categories = categories)

@app.route('/alladvices')
def allAdvices():
	advices = session.query(Advice).order_by(Advice.title.asc()).all()
	return render_template('allAdvices.html', advices = advices)

@app.route('/category/new', methods = ['GET', 'POST'])
def newCategory():
	if request.method == 'POST':
		if request.form['name']:
			newCat = Category(name = request.form['name'])
			session.add(newCat)
			session.commit()
			return redirect(url_for('allCategories'))
	else:
		return render_template('newCategory.html')

@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/advice')
def category(category_id):
	advices = session.query(Advice).filter_by(category_id = category_id).order_by(Advice.title.asc()).all()
	category = session.query(Category).filter_by(id = category_id).one()
	return render_template('category.html',category = category, advices = advices)

@app.route('/categories/<int:category_id>/edit', methods = ['GET', 'POST'])
def editCategory(category_id):
	editedCat = session.query(Category).filter_by(id  = category_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedCat.name = request.form['name']
			session.add(editedCat)
			session.commit()
			return redirect(url_for('allCategories'))
	else:
		return render_template('editCategory.html', category = editedCat)


@app.route('/categories/<int:category_id>/delete', methods = ['GET', 'POST'])
def deleteCategory(category_id):
	deletedCat = session.query(Category).filter_by(id  = category_id).one()
	if request.method == 'POST':
		session.delete(deletedCat)
		session.commit()
		return redirect(url_for('allCategories'))
	else:
		return render_template('deleteCategory.html', category = deletedCat)

@app.route('/categories/<int:category_id>/advice/new', methods = ['GET', 'POST'])
def newAdvice(category_id):
	if request.method == 'POST':
		if request.form['title'] and request.form['body']:
			newAd = Advice(title = request.form['title'], body = request.form['body'], category_id = category_id)
			session.add(newAd)
			session.commit()
			return redirect(url_for('category', category_id = category_id))
	else:
		return render_template('newAdvice.html', category_id = category_id)

@app.route('/categories/<int:category_id>/advices/<int:advice_id>/delete', methods = ['GET', 'POST'])
def deleteAdvice(category_id, advice_id):
	deletedAd = session.query(Advice).filter_by(category_id  = category_id,id = advice_id).one()
	if request.method == 'POST':
		session.delete(deletedAd)
		session.commit()
		return redirect(url_for('category',category_id = category_id))
	else:
		return render_template('deleteAdvice.html', advice = deletedAd)

@app.route('/categories/<int:category_id>/advices/<int:advice_id>/edit', methods = ['GET', 'POST'])
def editAdvice(category_id, advice_id):
	editedAd = session.query(Advice).filter_by(category_id  = category_id,id = advice_id).one()
	if request.method == 'POST':
		if request.form['title'] and request.form['body']:
			editedAd.title = request.form['title']
			editedAd.body = request.form['body']
			session.add(editedAd)
			session.commit()
			return redirect(url_for('category',category_id = category_id))
	else:
		return render_template('editAdvice.html', advice = editedAd)


if __name__ == '__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run(host='0.0.0.0',port = 5000)