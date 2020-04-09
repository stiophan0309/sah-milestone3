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
    return render_template("experience.html", my_experience=mongo.db.experience.find())

@app.route('/education')
def education():
    return render_template("education.html", my_education=mongo.db.education.find())

@app.route('/admin')
def admin():
    return render_template("admin.html",
    blog=mongo.db.blog.find())

@app.route('/blog')
def blog():
    return render_template("blog.html", my_blog=mongo.db.blog.find())

@app.route('/blog/add', methods=['POST'])
def add ():
    blog = mongo.db.blog
    blog.insert_one(request.form.to_dict())
    return redirect(url_for('blog'))

@app.route('/blog/edit')
def edit():
    return render_template("editblog.html",
    my_blog=mongo.db.blog.find())

@app.route('/blog/update/<blog_id>', methods=['POST'])
def update(blog_id):
    mongo.db.blog.update(
        {'_id': ObjectId(blog_id)}, {
        'blog_title': request.form.get('blog_title'),
        'blog_content': request.form.get('blog_content')
    })
    return redirect(url_for('blog'))

@app.route('/blog/delete/<blog_id>')
def delete(blog_id):
    mongo.db.blogs.remove({'_id': ObjectId(blog_id)})
    return redirect(url_for('blog'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=True)
