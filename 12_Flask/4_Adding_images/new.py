# IMPORTING
from flask import Flask, render_template
import os

# INTERACTION
app = Flask(__name__)

picfolder = os.path.join('static')  # locate the folder
app.config['UPLOAD_FOLDER'] = picfolder  # upload folder


# MAPPING
@app.route('/')
# INPUTS
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'goku.jpg')
    return render_template('home.html', user_image=pic)


# MAPPING
@app.route('/second')
# INPUTS
def second():
    # return "<h1>Welcome to second page</h1>"
    return render_template('second.html')


# MAIN
if __name__ == '__main__':
    app.run(debug=True)
