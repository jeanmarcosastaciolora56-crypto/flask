from flask import Flask, render_template
app=Flask (__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/recordar")
def recordar():
    return render_template("remember.html")

@app.route("/registro")
def registrar():
    return render_template("sign_up.html")

@app.route("/nowei", methods=['POST'])
def mentira():
    return render_template("loginxd.html")

if __name__ == "__main__":
    app.run(debug=True)