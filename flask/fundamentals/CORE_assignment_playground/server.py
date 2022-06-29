from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", num=3, color="rgb(57, 255, 248)")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("index.html", num=num, color="rgb(57, 255, 248)")

@app.route('/play/<int:num>/<string:color>')
def num_color_boxes(num,color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

