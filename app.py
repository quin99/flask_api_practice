from flask import Flask, jsonify, request

app = Flask(__name__)

# Default routes
@app.route('/')
def hello_world():
	return 'Hello World!'

# Very simple API
@app.route('/super_simple')
def super_simple():
	return jsonify(message='Hello from the Planetary API')


# Working with HTTP status codes
@app.route('/not_found')
def not_found():
	return jsonify(message='That resource was not found'), 404


# Working with URL Parameters
@app.route('/parameters')
def parameters():
	name = request.args.get('name')
	age = int(request.args.get('age'))
	if age < 18:
		return jsonify(message="Sorry" + name + ", you are not old enough")
	else:
		return jsonify(message="Welcome " + name)


# Working with URL Variables and Conversion Filters
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
	if age < 18:
		return jsonify(message="Sorry" + name + ", you are not old enough")
	else:
		return jsonify(message="Welcome " + name)


# Run
if __name__ == '__main__':
	app.run()
