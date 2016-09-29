from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
       #only works for POST
    return render_template("index.html")

@app.route("/auth", methods=["GET", "POST"])
def ausdg():
        #print "***DIAG: this Flask obj ***"
        #print app
        #print "***DIAG: request obj ***"
        #print request

        if request.method=="POST":
            if request.form["username"]=="Kathy" and request.form['pazz']=="123":
                return render_template("success.html", user=request.form["username"])
            else:
                return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
