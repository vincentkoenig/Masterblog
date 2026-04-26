from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        posts = load_posts()
        new_id = posts[-1]["id"] + 1
        new_post = {"id": new_id, "title": title, "author": author, "content": content}
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)