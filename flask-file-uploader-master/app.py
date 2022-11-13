from flask import Flask, request, render_template, flash
from flask_bootstrap import Bootstrap
from image_processor import final_measurement
import requests
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

files_url = "https://app.simplefileupload.com//api/v1/files"


@app.route('/', methods=['POST'])
def get_arguments():
    gender = request.form.get('Genero')
    age = request.form.get('idade')
    print(gender)
    print(age)
    files_uploaded = get_files_uploaded()
    if len(files_uploaded) == 2:
        if 'moeda.jpg' in files_uploaded[0]:
            logging.debug('The coin image is at the position 0. Refactoring the list...')
            coin_img = files_uploaded.pop(0)
            files_uploaded.append(coin_img)
            final_measurement.get_circumference(files_uploaded, int(age), gender)
        else:
            final_measurement.get_circumference(files_uploaded, int(age), gender)
    elif len(files_uploaded) > 2:
        logging.debug('The list contains more than one baby image. Reprocessing the list...')
        for i in range(0, len(files_uploaded)):
            if 'moeda.jpg' not in files_uploaded[i]:
                logging.debug('Coin image not found! Checking again...')
            else:
                coin_img = files_uploaded.pop(i)
                files_uploaded.reverse()
                last_baby_img = files_uploaded.pop(0)
                for t in range(0, len(files_uploaded)):
                    remove_baby_at_any_time()
                new_images = [last_baby_img, coin_img]
                final_measurement.get_circumference(new_images, int(age), gender)
    else:
        message = 'Nenhuma imagem enviada! Envie uma imagem para que os cálculos possam ser realizados.'
        flash(message)
    return render_template('index.html')


def get_files_uploaded():
    files = []
    request_baby = requests.get(files_url,
                                auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
    for x in request_baby.json().get('data'):
        if x.get('attributes').get('filename') != 'moeda':
            baby_url = x.get('attributes').get('cdn-url')
            files.append(baby_url)
            logging.debug(baby_url)
        else:
            coin_url = x.get('attributes').get('cdn-url')
            files.append(coin_url)
            logging.debug(coin_url)
    return files


@app.route('/deleteImage', methods=['POST'])
def remove_baby_at_any_time():
    files = []
    request_baby = requests.get(files_url,
                                auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
    for x in request_baby.json().get('data'):
        if x.get('attributes').get('filename') != 'moeda':
            baby_url = x.get('attributes').get('cdn-url')
            files.append(baby_url)
            logging.debug(baby_url)
        else:
            coin_url = x.get('attributes').get('cdn-url')
            files.append(coin_url)
            logging.debug(coin_url)
    if len(files) > 1:
        if 'moeda' not in files[1]:
            requests.delete("https://app.simplefileupload.com/api/v1/file?url={}".format(files[1]),
                            auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
            message = 'Imagem do bebê deletada! Prossiga com o envio de uma nova imagem.'
            flash(message)
        else:
            requests.delete("https://app.simplefileupload.com/api/v1/file?url={}".format(files[0]),
                            auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
            message = 'Imagem do bebê deletada! Prossiga com o envio de uma nova imagem.'
            flash(message)
    else:
        logging.debug('No images found!')
        message = 'Erro: Não há imagens para remover.'
        flash(message)
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/SaibaMais', methods=['GET', 'POST'])
def SaibaMais():
    return render_template('saibaMais.html')


@app.route('/Example', methods=['GET', 'POST'])
def Example():
    return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True)
