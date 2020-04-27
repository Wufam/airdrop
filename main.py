# -*- coding: utf-8 -*-
import os

from flask import Flask, send_file, send_from_directory, current_app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename


# Иницилизация фласка в переменную app
app = Flask(__name__)


# Корневая (стартовая) страничка, которагя загружает файлы в директорию upload
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		f = request.files['file']
		f.save(u'upload/' + f.filename)
	return render_template('index.html')


# Страничка загрузки, которая выводит список загруженных файлов
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	directory = "upload/"
	file = os.listdir(directory)
	return render_template('upload.html', my_list=file)


# Генерирует ссылки для скачивания относительно пути котрый указан
@app.route('/upload/<path:filename>', methods=['GET', 'POST'])
def download(filename):
	return send_from_directory(directory='upload/', filename=filename)


# Запуск
if __name__ == "__main__":
	app.run(host="0.0.0.0",port="80")
