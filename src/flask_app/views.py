from model.functions import pred
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from settings import UPLOAD_FOLDER

flask_app = Blueprint(name="flask_app", import_name=__name__)

@flask_app.route( '/', methods=["GET", "POST"] )
def index( ):
    
    image = None

    return render_template( 'index.html', image = image )

@flask_app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['file']
    
    if not pic:
        return 'No pic uploaded!', 400
    
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    if not filename or not mimetype:
        return 'Bad upload!', 400

    pic.save(os.path.join(UPLOAD_FOLDER, secure_filename(pic.filename)))

    return redirect( url_for('flask_app.predict',filename = filename) )

@flask_app.route('/predict/<filename>', methods = ['GET'] )
def predict( filename ):
    results = pred( str(filename) )
    results = {key: round(value * 100, 2) for key, value in results.items()}
    #print(results)

    image = f'/static/upload/{filename}'

    return render_template( 'predict.html', results = results, image = image )

