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


def fetch_post_by_id(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None

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
        new_post = {"id": new_id, "title": title, "author": author, "content": content, "likes": 0}
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            save_posts(posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        posts = load_posts()
        for post in posts:
            if post["id"] == post_id:
                post["title"] = title
                post["author"] = author
                post["content"] = content
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>')
def like(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
    save_posts(posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)