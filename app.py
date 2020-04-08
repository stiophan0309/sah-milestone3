import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'SAH_Milestone3'
app.config["MONGO_URI"] = 'mongodb+srv://stiophan0309:Sleaghach0309@myfirstcluster-s3wmx.mongodb.net/SAH_Milestone3?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def home():
    # Open Home page
    return render_template("base.html")

@app.route("/index")
def index():
    # Open Home page
    return render_template("index.html")

@app.route("/contact")
def contact():
    # Open Contact page
    return render_template("contact.html")

@app.route('/get_skills')
def get_skills():
    return render_template("skills.html", skills=mongo.db.skills.find())

@app.route('/experience')
def experience():
    return render_template("experience.html", skills=mongo.db.experience.find())

@app.route('/education')
def education():
    return render_template("education.html", skills=mongo.db.education.find())

@app.route('/blog')
def blog():
    return render_template("blog.html", entry=mongo.db.blog.find())

@app.route('/admin')
def admin():
    return render_template("admin.html",
    blog=mongo.db.blog.find())

@app.route('/insert_blog', methods=['POST'])
def insert_blog():
    blog = mongo.db.blog
    blog.insert_one(request.form.to_dict())
    return redirect(url_for('blog'))

@app.route('/edit_blog')
def edit_blog():
    return render_template("editblog.html",
    entry=mongo.db.blog.find())

@app.route('/update_blog/<blog_id>', methods=['POST'])
def update_blog(blog_id):
    mongo.db.blog.update(
        {'_id': ObjectId(blog_id)}, {
        'blog_title': request.form.get('blog_title'),
        'blog_content': request.form.get('blog_content')
    })
    return redirect(url_for('blog'))

@app.route('/delete_blog/<blog_id>')
def delete_blog(blog_id):
    mongo.db.blogs.remove({'_id': ObjectId(blog_id)})
    return redirect(url_for('blog'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=True)
