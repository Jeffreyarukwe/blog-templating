from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", posts=data)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    for blog_post in all_posts:
        if blog_post["id"] == blog_id:
            return render_template("post.html", dt=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
