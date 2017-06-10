from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<template>")
def hello(template):
    return render_template(template + ".html", a = 5, text=1000)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
