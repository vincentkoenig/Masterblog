from flask import Flask
from flask import render_template
import json
app = Flask(__name__)


def load_posts():
    with open("blog_post.json", "r") as fileobj:
        post = json.load(fileobj)
        return post


def save_posts(posts):
    with open("blog_post.json", "w") as fileobj:
        json.dump(posts, fileobj)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)