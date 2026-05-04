from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)


def load_posts():
    try:
        with open("blog_post.json", "r") as fileobj:
            post = json.load(fileobj)
            return post
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_posts(posts):
    with open("blog_post.json", "w") as fileobj:
        json.dump(posts, fileobj, indent=4)


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

        if not title or not author or not content:
            return render_template('add.html')

        posts = load_posts()
        max_id = max((post["id"] for post in posts), default=0)
        new_id = max_id + 1
        new_post = {"id": new_id, "title": title, "author": author, "content": content, "likes": 0}
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    posts = load_posts()
    posts = [post for post in posts if post["id"] != post_id]
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

        if not title or not author or not content:
            return render_template('update.html', post=post)

        posts = load_posts()
        for post in posts:
            if post["id"] == post_id:
                post["title"] = title
                post["author"] = author
                post["content"] = content
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
    save_posts(posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)