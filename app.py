from flask import Flask,render_template

app = Flask(__name__, template_folder='Templates')


@app.route("/")
def Ride_away():
  return render_template("homepage.html")

if __name__== "__main__":
  app.run(host="0.0.0.0", debug = True)
