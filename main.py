import logging
from flask import Flask

app = Flask(__name__)

@app.route('/rahul')
def hello('/rahul'):
	return 'Hello there'

if __name__ == '__main__':
	app.run()
