from flask import Flask
from flask import render_template

app = Flask(__name__)

#Conexion con base de datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSDWORD'] = ''
app.config['MYSQL_DATABASE_DATABASE'] = 'sistema'
mysql.app_init(app)




#Ruteo de mis páginas.
@app.route('/')
def index():
    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug = True)