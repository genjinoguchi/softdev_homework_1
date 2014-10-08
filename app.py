#whooooooooooooop swaggiest team ever
from flask import Flask, render_template, request

app = Flask(__name__)
query = ""


@app.route("/<hurrdurr>")
def index(hurrdurr=None):
    return render_template("index.html",
                           query=query)


@app.route("/query", methods=['POST'])
def readQuery():
    if request.method=="POST":
        print "Query received : "+request.form["query"]
    return redirect("")



if __name__ == "__main__":
    app.debug=True
    app.run()
