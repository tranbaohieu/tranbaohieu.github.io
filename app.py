import os
from flask import Flask, render_template, request, redirect, url_for
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)

@app.route('/')
def home():
    """Display a list of all blog posts."""
    posts = [p for p in pages]
    return render_template("index.html", posts=posts)

@app.route('/post/<path:path>/')
def post(path):
    """Render a blog post from Markdown to HTML."""
    post = pages.get_or_404(path)
    return render_template("post.html", post=post)

@app.route('/write', methods=['GET', 'POST'])
def write():
    """Write a new blog post manually (Markdown format)."""
    if request.method == 'POST':
        title = request.form['title'].replace(" ", "_")
        content = request.form['content']
        post_path = os.path.join("content", f"{title}.md")

        # Save Markdown content
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(f"title: {title}\n\n{content}")

        return redirect(url_for('post', path=title))

    return render_template("write.html")

if __name__ == '__main__':
    app.run(debug=True)
