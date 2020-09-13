from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_index():
    '''Return the view of the home page.'''
    return render_template("index.html")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
