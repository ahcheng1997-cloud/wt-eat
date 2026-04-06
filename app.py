from flask import Flask, request
import os

app = Flask(**name**)

@app.route("/", methods=["GET"])
def home():
return "OK"

@app.route("/", methods=["POST"])
def webhook():
return "OK"

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
