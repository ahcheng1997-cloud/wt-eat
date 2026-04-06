from flask import Flask
import os

app = Flask(**name**)

@app.route("/")
def home():
return "OK"

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
