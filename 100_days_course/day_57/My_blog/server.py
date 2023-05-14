from flask import Flask, render_template
from post import Post
import requests

test_blog = "https://api.npoint.io/f7f6e4e257855fc21f9b"
posts = requests.get(test_blog).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:num>")
def get_post(num):
    chosen_post = [post for post in post_objects if post.id == num][0]
    return render_template("post.html", posts=chosen_post)


@app.route("/guess/<name>")
def guess(name):
    param = {
        "name": name
    }
    gender_response = requests.get(url="https://api.genderize.io", params=param).json()
    age_response = requests.get(url="https://api.agify.io", params=param).json()
    return render_template("guess.html", name=name, gender=gender_response["gender"], years_old=age_response["age"])


@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/f7f6e4e257855fc21f9b"
    all_posts = requests.get(url=blog_url).json()
    return render_template("blog.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
