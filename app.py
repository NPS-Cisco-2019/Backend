import flask

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello world")

app.run(debug=True)
@app.route("/Firefox")
@app.route("/Chrome")
@app.route("/Safari")
@app.route("/Picture")
@app.route("/Answer")
@app.route("/Settings")
@app.route("/Saved Answers")
@app.route("/GradeChoice")
@app.route("/Tutorial")
