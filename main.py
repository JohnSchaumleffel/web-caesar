from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0"/>
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit" />
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrpyt():
    rot_input = int(request.form['rot'])
    text_input = request.form['text']
    rotated = rotate_string(text_input, rot_input)
    return form.format(rotated)

app.run()