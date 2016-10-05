from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def add(name, pazz, file):
    f = open(file, 'a+')
    myHashObj = hashlib.sha1(pazz)
    pazz = myHashObj.hexdigest()
    lines = f.readlines()
    for line in lines:
        print "LINE " + line
        for names in line.split(','):
            if name == names[0]:
                return False
    f.write(name + ',' + pazz + "\n")
    return True

def verify(name, pazz, file):
    f = open(file, 'r')
    lines = f.readlines()
    myHashObj = hashlib.sha1(pazz)
    pazz = myHashObj.hexdigest()
    for line in lines:
        if name == line.split(',')[0]:
            return line.split(',')[1].replace('\n','') == pazz


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method=="POST":
        user = request.form["username"]
        pazz = request.form["pazz"]
        if add(user, pazz, '/data/auth.txt'):
            return render_template("success.html", user=user)
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
        if request.method=="POST":
            user = request.form["username"]
            pazz = request.form["pazz"]
            if verify(user, pazz, "/data/auth.txt"):
                session["username"] = user
                return "works"
            else:
                return "no"
        else:
            if "username" in session:
                return "works"
            else:
                return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
