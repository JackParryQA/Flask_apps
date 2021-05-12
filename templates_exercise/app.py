from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    list_1=["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('index.html', users=list_1)

if __name__ == "__main__":
    app.run(debug=True)