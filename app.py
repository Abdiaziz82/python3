from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My first Time learning Flask"

@app.route('/about')
def about_page():
    return "this is the about page"

@app.route('/about/home')
def about_home():
    return "this is the about on home page"

@app.route('/<string:name>')
def user_profile(name):
    return f"Welcome {name}"

@app.route('/courses/<int:course_id>')
def course_details(course_id):
    return f"welcome to the modules {course_id}"

if __name__ == "__main__":
    app.run(port = 5002, debug = True)