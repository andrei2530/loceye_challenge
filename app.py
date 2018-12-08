import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import imgproc

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(basedir,app.config['UPLOAD_FOLDER'],filename)
            palette = imgproc.get_palette(image_path)          
            return render_template('result.html',imgpath = os.path.join('/',app.config['UPLOAD_FOLDER'],filename),hex_list = palette)

    return render_template('main_page.html')
    
    








