from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, request
app = Flask(__name__)
cluster=MongoClient("mongodb+srv://vaishnav:vaishnav@cluster0.tzdx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["vaishnav"]
collection = db["portfolio"]
collection.insert_one({"name": "vaishnav", "email": "vaishnavanand90@gmail.com", "message": "hello"})

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['POST'])
def contact():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('_replyto')
    message = request.form.get('message')
    collection.insert_one({"name": name, "email": email, "message":message})
    return "Form submitted!", 200
if __name__ == '__main__':
    app.run(debug=True, port = 5000)
