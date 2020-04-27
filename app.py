import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import datetime
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'SAH_Milestone3'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def index():
    """ Open Home page """
    return render_template("index.html", my_experience=mongo.db.experience.find(), my_education=mongo.db.education.find())

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """ Open Contact page """
    return render_template("index.html")
    
@app.route('/blog')
def blog():
    """ Open Blog page """
    return render_template("blog.html", my_blog=mongo.db.blog.find())

@app.route('/blog/add', methods=['GET', 'POST'])
def add():
    """ Create a new blog post """
    blog = mongo.db.blog
    blog.insert_one({
        "blog_title": request.form.get("blog_title"),
        "blog_author": request.form.get("blog_author"),
        "blog_content": request.form.get("blog_content"),
        "date_created": datetime.datetime.now()
    })
    return redirect(url_for('blog'))

@app.route('/blog/edit')
def edit():
    """ Open the Blog Edit/Delete Page """
    return render_template("editblog.html",
    my_blog=mongo.db.blog.find())

@app.route('/blog/update/<blog_id>', methods=['POST'])
def update(blog_id):
    """ Edit an existing Blog post and be redirected to the Blog page """
    mongo.db.blog.update(
        {'_id': ObjectId(blog_id)}, 
        { '$set':
            {
            'blog_title': request.form.get('blog_title'),
            'blog_content': request.form.get('blog_content'),
            'last_updated': datetime.datetime.utcnow()
            }
        }
    )
    return redirect(url_for('blog'))

@app.route('/blog/delete/<blog_id>')
def delete(blog_id):
    """ Delete an existing Blog post and be redirected to the Blog page """
    mongo.db.blog.remove({'_id': ObjectId(blog_id)})
    return redirect(url_for('blog'))

@app.route('/admin')
def admin():
    """ Open the Admin page for creating/deleting and updating Blog posts """
    return render_template("admin.html",
    blog=mongo.db.blog.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=True)
