#whooooooooooooop swaggiest team ever
from flask import Flask, render_template, request, redirect

from search import getAnswers

app = Flask(__name__)
query = ""


@app.route("/")
def index():
        return render_template("index.html",query="",header="",results={},size=0)

@app.route("/<hurrdurr>")
def search(hurrdurr=None):
        header='"'+hurrdurr+'"'+" received these results: "
        results=getAnswers(hurrdurr)
        hurrdurr+=" | "
        return render_template("index.html",query=hurrdurr,header=header,results=results,size=0)


@app.route("/query", methods=['POST'])
def readQuery():
        if request.method=="POST":
                print "Query received : "+request.form["query"]
                return redirect("/"+request.form["query"])



if __name__ == "__main__":
        app.debug=True
        app.run()
