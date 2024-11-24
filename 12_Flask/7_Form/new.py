# IMPORTING
from flask import Flask, render_template, request

# INTERACTION
app = Flask(__name__)

# MAPPING
@app.route('/')
# @app.route('/homepage')
# INPUTS
def homepage():
    return render_template("index.html")


@app.route('/confirmation', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        n = request.form.get('name')
        p = request.form.get('phoneNumber')
        db = request.form.get('dob')
        e = request.form.get('email')
        return render_template('confirm.html', name=n, phoneNumber=p, dob=db, email=e)

# MAIN
if __name__ == '__main__':
    app.run(debug=True)