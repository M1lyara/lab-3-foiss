from flask import Flask, render_template 

app = Flask(__name__, template_folder='C:/Users/Lenovo/Desktop/lab 3/templates')

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)