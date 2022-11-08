import os
import PIL
from PIL import Image
import simplejson
import traceback

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

import final_measurement
from lib.upload_file import uploadfile

<<<<<<< Updated upstream
=======
import requests
import json

>>>>>>> Stashed changes
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_FOLDER'] = 'resources/images/'
app.config['THUMBNAIL_FOLDER'] = 'resources/thumbnail/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
IGNORED_FILES = set(['.gitignore'])

bootstrap = Bootstrap(app)

gender = ""
age = ""
<<<<<<< Updated upstream
=======
files_url = "https://app.simplefileupload.com//api/v1/files"
>>>>>>> Stashed changes


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def gen_file_name(filename):
    i = 1
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        name, extension = os.path.splitext(filename)
        filename = '%s_%s%s' % (name, str(i), extension)
        i += 1

    return filename


def create_thumbnail(image):
    base_width = 80
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image))
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
    img.save(os.path.join(app.config['THUMBNAIL_FOLDER'], image))

    return True


@app.route('/', methods=['POST'])
def get_arguments():
    global gender
    global age
    gender = request.form.get('Genero')
    age = request.form.get('idade')
    print(gender)
    print(age)
<<<<<<< Updated upstream
    return render_template('index.html')


@app.route("/upload", methods=['GET', 'POST'])
=======
    files_uploaded = get_files_uploaded()
    final_measurement.get_circumference(files_uploaded, int(age), gender)
    return render_template('index.html')


def get_files_uploaded():
    files = []
    request_baby = requests.get(files_url, auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
    for x in request_baby.json().get('data'):
        if x.get('attributes').get('filename') != 'moeda':
            baby_url = x.get('attributes').get('cdn-url')
            files.append(baby_url)
            print(baby_url)
        else:
            coin_url = x.get('attributes').get('cdn-url')
            files.append(coin_url)
            print(coin_url)
    return files


'''@app.route("/upload", methods=['GET', 'POST'])
>>>>>>> Stashed changes
def upload():
    if request.method == 'POST':
        files = request.files['file']

        if files:
            filename = secure_filename(files.filename)
            filename = gen_file_name(filename)
            mime_type = files.content_type

            if not allowed_file(files.filename):
                result = uploadfile(name=filename, type=mime_type, size=0, not_allowed_msg="File type not allowed")

            else:
                uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print(filename)
                files.save(uploaded_file_path)
                final_measurement.get_circumference(filename, int(age), gender)

                if mime_type.startswith('image'):
                    create_thumbnail(filename)

                size = os.path.getsize(uploaded_file_path)

                result = uploadfile(name=filename, type=mime_type, size=size)

            return simplejson.dumps({"files": [result.get_file()]}), filename

    if request.method == 'GET':
        files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if
                 os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f)) and f not in IGNORED_FILES]

        file_display = []

        for f in files:
            size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], f))
            file_saved = uploadfile(name=f, size=size)
            file_display.append(file_saved.get_file())

        return simplejson.dumps({"files": file_display})

    return redirect(url_for('index'))


@app.route("/delete/<string:filename>", methods=['DELETE'])
def delete(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file_thumb_path = os.path.join(app.config['THUMBNAIL_FOLDER'], filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)

            if os.path.exists(file_thumb_path):
                os.remove(file_thumb_path)

            return simplejson.dumps({filename: 'True'})
        except:
            return simplejson.dumps({filename: 'False'})


@app.route("/resources/thumbnail/<string:filename>", methods=['GET'])
def get_thumbnail(filename):
    return send_from_directory(app.config['THUMBNAIL_FOLDER'], filename=filename)


@app.route("/resources/images/<string:filename>", methods=['GET'])
def get_file(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename=filename)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
