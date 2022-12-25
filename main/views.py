from flask import render_template, Blueprint, request
from functions import search_text
import logging

main_blueprint = Blueprint('main_blueprint', __name__)
logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    text_search = request.args['s']
    #logging.info(f"Запрос: {text_search}")
    search_data = search_text(text_search)
    return render_template("post_list.html", search_data=search_data, text_search=text_search)


# @messages_blueprint.route('/inbox')
# def inbox_page():
#     return "Это страничка входящих сообщений"
#
# @messages_blueprint.route('/sent')
# def sent_page():
#     return "Это страничка отправленных сообщений"
#