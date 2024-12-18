from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, request
app = Flask(__name__)
cluster=MongoClient("mongodb+srv://vaishnav:vaishnav@cluster0.tzdx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["vaishnav"]
collection = db["portfolio"]
collection2 = db["ratings"]
collection.insert_one({"name": "vaishnav", "email": "vaishnavanand90@gmail.com", "message": "hello"})
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('_replyto')
    message = request.form.get('message')
    collection.insert_one({"name": name, "email": email, "message":message})
    return "Form submitted!", 200
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Anonymous') 
    rating = request.form.get('rating', type=int)
    opinion = request.form.get('opinion')
    collection2.insert_one({"name": name, "rating": rating, "opinion": opinion})
    sorted_comments = collection2.find().sort("rating", -1)
    print(sorted_comments)
    return render_template('form.html', sorted_comments=sorted_comments)
    # return "Form submitted!", 200
@app.route('/review')
def review():
    sorted_comments = collection2.find().sort("rating", -1)
    return render_template('form.html', sorted_comments = sorted_comments)
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact2')
def contact2():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True, port = 5000)


