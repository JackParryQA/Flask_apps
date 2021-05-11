from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello World!\nThis is the home page'

@app.route('/about')
def about():
    return 'Hello World!\nThis is the about page'

@app.route('/squared/<int:num>')
def squared(num):
    return str(num**2)

if __name__ == "__main__":
    app.run(debug=True)