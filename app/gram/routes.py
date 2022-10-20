from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from app.models  import Post
from .forms import CreatePostForm

gram = Blueprint('gram', __name__, template_folder='gram_templates')

@gram.route('/posts/create', methods=["GET", "POST"])
@login_required
def createPost():
    form = CreatePostForm()
    if request.method == "POST":
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            post = Post(title, img_url, caption, current_user.id)

            post.saveToDB()

            return redirect(url_for('homePage'))

    return render_template('create_post.html', form=form)

@gram.route('/posts')
def viewPosts():
    posts = Post.query.order_by(Post.date_created).all()[::-1]
    return render_template('feed.html', posts=posts)