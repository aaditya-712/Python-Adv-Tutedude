# IMPORTING
from flask import Flask, render_template

# INTERATION
web = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/home')

# INPUTS
def home():
    return "Welcome"

# MAIN
if __name__ == "__main__":
    web.run(debug=True)