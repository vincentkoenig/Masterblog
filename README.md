# Masterblog 📝

A full-stack blog application built with **Python** and **Flask** — create, read, update, delete, and like blog posts through a clean web interface.

## Features

- ✍️ **Create** new blog posts with title, author, and content
- 📖 **Read** all posts on the home page
- ✏️ **Update** existing posts
- 🗑️ **Delete** posts
- ❤️ **Like** posts with a like counter
- 💾 JSON-based data persistence

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

## Project Structure

```
Masterblog/
├── app.py              # Flask application & routes
├── blog_post.json      # JSON data storage
├── static/             # CSS styles
└── templates/          # Jinja2 HTML templates
    ├── index.html
    ├── add.html
    └── update.html
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Masterblog.git
cd Masterblog
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in your browser**
```
http://localhost:5000
```

## What I Learned

- Building REST-style routes with Flask (`GET`, `POST`)
- Handling HTML forms and user input server-side
- Persisting data with JSON file storage
- Rendering dynamic content with Jinja2 templates
- Implementing full CRUD functionality from scratch
