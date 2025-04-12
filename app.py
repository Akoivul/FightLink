import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
import config
import db
import items
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_items = items.get_items()
    return render_template("index.html", items=all_items)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    items = users.get_items(user_id)
    return render_template("show_user.html", user=user, items=items)

@app.route("/find_item")
def find_item():
    query = request.args.get("query")
    if query:
        results = items.find_items(query)
    else:
        query = ""
        results = []
    return render_template("find_item.html", query=query, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    return render_template("show_item.html", item=item)

@app.route("/new_item")
def new_item():
    require_login()
    return render_template("new_item.html")

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    game_name = request.form["game_name"]
    if not game_name or len(game_name) > 100:
        abort(403)
    game_username = request.form["game_username"]
    if not game_username or len(game_username) > 50:
        abort(403)
    availability_time = f"{request.form['availability_start']}-{request.form['availability_end']}"
    availability_start = request.form["availability_start"]
    availability_end = request.form["availability_end"]
    platform = request.form["platform"]
    region = request.form["region"]
    other_info = request.form["other_info"]
    if len(other_info) > 1000:
        abort(403)
    user_id = session["user_id"]

    items.add_item(game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info, user_id)

    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_item.html", item=item)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    game_name = request.form["game_name"]
    if not game_name or len(game_name) > 100:
        abort(403)
    game_username = request.form["game_username"]
    if not game_username or len(game_username) > 50:
        abort(403)
    availability_time = f"{request.form['availability_start']}-{request.form['availability_end']}"
    availability_start = request.form["availability_start"]
    availability_end = request.form["availability_end"]
    platform = request.form["platform"]
    region = request.form["region"]
    other_info = request.form["other_info"]
    if len(other_info) > 1000:
        abort(403)

    items.update_item(item_id, game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info)

    return redirect("/item/" + str(item_id))

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "ERROR: passwords do not match"

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "ERROR: username is already taken"

    return render_template("user_created.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "ERROR: wrong username or password"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")

