from flask import Flask 
app = Flask(__name__)


@app.route('/test')
def test():
    return '<h1>hello class</h1>'
# @app.route("/")
# @app.route("/home")
# def home():
#     return "<h1>Home Page</h1>"


# @app.route("/about")
# def about():
#     return "<h1>About Page</h1>"

# @app.route('/test')
# def myfun():
#     return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.run(debug=True)



