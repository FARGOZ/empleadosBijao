from flask import Flask
from flask import render_template

app = Flask(__name__)

#Ruteo de mis páginas.
@app.route('/')
def index():
    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug = True)