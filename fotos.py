import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request,redirect,url_for, flash,jsonify,session
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "app/static/uploads"

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg', 'gif'])

csrf=CSRFProtect() 

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gatito'
app.config['MYSQL_DB'] = 'buerreras'

db=MySQL(app)
app.secret_key='mysecretkey'

def allowed_file(file):
   file=file.split('.')
   if file[1] in ALLOWED_EXTENSIONS:
     return True
   return False


@app.route('/upload', methods=["POST"])
def upload():
   file = request.files["uploaadFile"]
   print(file,file.filename)
   filename = secure_filename(file.filename)
   print(filename)
   if file and allowed_file(filename):
      print("Permitido")
   file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
   return 'Guardado correctamente'


@app.route('/')
def index():
    return render_template('fomularioF.html')



if __name__ == '__main__':
 app.run(debug=True, port=8000)




