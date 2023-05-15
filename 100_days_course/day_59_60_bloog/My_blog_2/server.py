from flask import Flask, render_template, request
from post import Post
import requests
import smtplib


EMAIL = "testowy100daysms@gmail.com"
PASSWORD = 'REMOVED'


test_blog = "https://api.npoint.io/c3947adcaad7da291c86"
posts = requests.get(test_blog).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["jpg"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=post_objects)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data)
        return render_template("contact.html", if_correct=True)
    return render_template("contact.html", if_correct=False)


def send_mail(data):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="testowy100daysms@gmail.com",
            msg=f"Subject:New mail from {data['name']}!\n\n"
                f"Name: {data['name']}\n"
                f"Email: {data['email']}\n"
                f"Phone: {data['phone']}\n"
                f"Message: {data['message']}")


@app.route("/post/<int:num>")
def get_post(num):
    chosen_post = [post for post in post_objects if post.id == num][0]
    return render_template("post.html", post=chosen_post)


if __name__ == "__main__":
    app.run(debug=True)
