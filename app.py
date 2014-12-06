# ------ Flask Hello World ----- #

# import the Flask class from the flask module #
from flask import Flask

# create the application object
app = Flask(__name__)

#error handling'
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
		return "Hello, World -- Now in debug!!"

#dynamic routes
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#integer value
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "integer"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "float"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "path value"

#new view
@app.route("/name/<name>")
def index(name):
	if name.lower() == "micheal" :
		return "hello {}".format(name)
	else :
		return "Not Found", 404


# start the development server using the run() method
if __name__ == "__main__":
	 app.run()
