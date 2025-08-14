from flask import Flask, redirect, request, render_template
import random
import string

from models import (
    init_db, 
    insert_url, 
    get_all_urls, 
    get_one_url_by_short_url,
    update_visit_count,
    delete_url
)

app = Flask(__name__)

init_db()

def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("original_url")
        short_url = generate_short_url()
        insert_url(original_url, short_url)
        return redirect("/")

    all_urls = get_all_urls()
    return render_template("index.html", all_urls=all_urls)

@app.route("/<short_url>")
def redirect_to_url(short_url):
    url_data = get_one_url_by_short_url(short_url)
    if url_data:
        update_visit_count(url_data[2])
        return redirect(url_data[1])

    return render_template("404.html"), 404

@app.route("/delete/<short_url>", methods=["POST"])
def delete(short_url):
    delete_url(short_url)
    return redirect("/")

@app.route("/about")
def about():
    return "This is a URL shortener application."

if __name__ == "__main__":
    app.run(debug=True)