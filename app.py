from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_session import Session
from threading import Thread

from config import ApplicationConfig
from route_register_user import register_user
from route_login import login
from route_logged_in import logged_in
from route_logout import logout
from route_admin_login import admin_login
from route_check_language import check_language
from route_set_language import set_language
from route_insert_contact_messages import insert_messages
from route_post_blog_posts import post_blog_posts
from route_get_blog_posts import get_blog_posts
from route_get_blog_post import get_blog_post
from route_insert_blog_post import insert_blog_post
from route_edit_blog_posts import edit_blog_posts
from route_get_contact_messages import get_messages
from route_delete_contact_messages import delete_messages
from route_get_chapters import get_chapters
from route_get_chapter import get_chapter
from route_get_vocab import get_vocab
from route_get_fill_in_blank import get_random_sentence
from route_admin import admin

app = Flask('')
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config.from_object(ApplicationConfig)

server_session = Session(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return "Naturally API"

@app.route('/register', methods = ['POST'])
def register():
    user = request.get_json()
    return register_user(user)

@app.route("/login", methods=["POST"])
def api_login():
    user = request.get_json()
    return login(user)

@app.route("/logged-in", methods=["GET"])
def api_logged_in():
    return logged_in()

@app.route("/logout", methods=["GET"])
def api_logout():
    return logout()

@app.route("/admin-login", methods=["POST"])
def api_admin_login():
    user = request.get_json()
    return admin_login(user)

@app.route("/admin", methods=["GET"])
def api_admin():
    return admin()

@app.route("/check-language", methods=["GET"])
def api_check_language():
    return check_language()

@app.route("/set-language", methods=["PUT"])
def api_set_language():
    language = request.get_json()
    return set_language(language)

@app.route("/blog/post", methods=["POST"])
def api_post_blog_posts():
    blog_post = request.get_json()
    return post_blog_posts(blog_post)

@app.route("/blog/get", methods=["GET"])
def api_get_blog_posts():
    return jsonify(get_blog_posts())

@app.route("/blog/get/<blog_post_id>", methods=["GET"])
def api_get_blog_post(blog_post_id):
    return jsonify(get_blog_post(blog_post_id))

@app.route("/blog/insert", methods=["POST"])
def api_insert_blog_post():
    blog_post = request.get_json()
    return insert_blog_post(blog_post)

@app.route("/blog/edit", methods=["PUT"])
def api_edit_blog_posts():
    blog_post = request.get_json()
    return jsonify(edit_blog_posts(blog_post))

@app.route("/contact", methods=["POST"])
def api_contact():
    message = request.get_json()
    return jsonify(insert_messages(message))

@app.route("/contact/admin", methods=["GET"])
def api_contact_admin():
    return jsonify(get_messages())

@app.route("/contact/delete/<id>", methods=["DELETE"])
def api_delete_messages(id):
    return delete_messages(id)

@app.route("/textbook/<language>", methods=["GET"])
def api_get_chapters(language):
    print("Request received")
    return jsonify(get_chapters(language))

@app.route("/textbook/<language>/<chapter>", methods=["GET"])
def api_get_chapter(language, chapter):
    return jsonify(get_chapter(language, chapter))

@app.route("/vocab/<language>/<chapter>", methods=["GET"])
def api_get_vocab(language, chapter):
    return jsonify(get_vocab(language, chapter))

@app.route("/exercises/fill-in-blank/<language>/<chapter>", methods=["GET"])
def api_get_fill_in_blank(language, chapter):
    return jsonify(get_random_sentence(language, chapter))

def run():
	app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()