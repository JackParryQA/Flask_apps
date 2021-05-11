from flask import Flask

app=Flask(__name__)

@app.route('/<int:num>')
def square(num):
    return str(num**2)

if __name__ == "__main__":
    app.run(debug=True)