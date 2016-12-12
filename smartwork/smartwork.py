from flask import Flask, render_template, request
from werkzeug.serving import run_simple
from smartwork_db import Survey, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime, time

engine = create_engine('sqlite:///smartwork.sqlite')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':

		ratings = request.form['ratings']
		comments = request.form['comments']
		team_id = request.form['team_id']

		newEntry = Survey(ratings=ratings, comments=comments, team_id=team_id)
		session.add(newEntry)
		session.commit()

		return render_template('ratings.html', ratings=ratings)

	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='14576', threaded=True)
    #app.run(host='127.0.0.1', port='14576')
    #app.run(host='0.0.0.0')

