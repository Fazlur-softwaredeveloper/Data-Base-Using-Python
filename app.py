from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory database (dictionary)
users = {
    "1001": {
        "name": "Ravi Kumar",
        "occupation": "Engineer",
        "phone": "9876543210",
        "email": "ravi@gmail.com",
        "address": "Chennai",
        "father": "Suresh Kumar",
        "mother": "Lakshmi"
    }
}

# Login credentials
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    result = None

    if request.method == "POST":
        uid = request.form["uid"]

        if uid in users:
            result = users[uid]
        else:
            users[uid] = {
                "name": request.form["name"],
                "occupation": request.form["occupation"],
                "phone": request.form["phone"],
                "email": request.form["email"],
                "address": request.form["address"],
                "father": request.form["father"],
                "mother": request.form["mother"]
            }
            result = users[uid]

    return render_template("dashboard.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

