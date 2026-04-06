from flask import Flask, request
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "XlA2IPfLH7iJYrdyzyQJ4nsO/z2QtvN9KDK5hF4lYSbDXFuBHjjba6RDGboj9b3L5blXJMrgYt8BRjpBxpRE4HEPIpyITY0IqMAuTcvfe1FCoFN309KkIAZosJJcjwUEmVLFDUxqoeLJYbAF5kxmeQdB04t89/1O/w1cDnyilFU="

@app.route("/", methods=["GET"])
def home():
return "OK"

@app.route("/", methods=["POST"])
def webhook():
return "OK"

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
