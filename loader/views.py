from flask import render_template, Blueprint, request
import logging
from functions import add_in_posts

loader_blueprint = Blueprint('loader_blueprint', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

logging.basicConfig(filename="basic.log", level=logging.INFO)
logging.basicConfig(filename="error.log", level=logging.ERROR)


@loader_blueprint.route('/add')
def add_page():
    return render_template("post_form.html")


@loader_blueprint.route('/upload_post', methods=['POST'])
def add_page_upload():
    text_post = request.form['content']
    picture = request.files.get("picture")
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        try:
            picture.save(f"./uploads/images/{filename}")
            add_in_posts(filename, text_post)
        except TypeError as e:
            logging.error(f"Картинка не загружена. Ошибка: {e}")
            print(e)
    else:
        logging.info(f"Картинка не загружена. Расширение: {extension}")
        print("Формат файла не поддерживается")
    return render_template("post_uploaded.html", pic=f"./uploads/images/{filename}", text=text_post)
