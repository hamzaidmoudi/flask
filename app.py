from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("base.html")
@app.route('/about')
def about():
    return render_template("about.html") 
@app.route('/articles')
def articles():
    return render_template("articles.html")
@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method=="POST":
       return "<h2> MESSAGE ENVOYE </h2>"  
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True, port=5004)
