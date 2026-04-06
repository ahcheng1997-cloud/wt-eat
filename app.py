from flask import Flask, request
import requests
import os

app = Flask(**name**)

CHANNEL_ACCESS_TOKEN = "你的token"

orders = []
menu = ["鍋貼", "水餃", "酸辣湯"]

# 👉 這行是關鍵（給 LINE 驗證用）

@app.route("/", methods=["GET"])
def home():
return "OK"

@app.route("/", methods=["POST"])
def webhook():
data = request.json

```
for event in data.get("events", []):
    if event["type"] == "message":
        reply_token = event["replyToken"]
        msg = event["message"]["text"]

        if msg == "八方":
            send_bafang_menu(reply_token)

        elif msg in menu:
            orders.append(msg)
            reply(reply_token, f"✅ 已點：{msg}")

        elif msg == "統計":
            summary = {}
            for item in orders:
                summary[item] = summary.get(item, 0) + 1

            if summary:
                text = "📊 統計：\n"
                for k, v in summary.items():
                    text += f"{k}：{v}\n"
            else:
                text = "目前沒人點"

            reply(reply_token, text)

        else:
            reply(reply_token, "輸入「八方」開始")

return "OK"
```

def send_bafang_menu(token):
flex = {
"type": "flex",
"altText": "菜單",
"contents": {
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{"type": "text", "text": "八方雲集", "weight": "bold", "size": "xl"},
{"type": "button", "action": {"type": "message", "label": "鍋貼", "text": "鍋貼"}},
{"type": "button", "action": {"type": "message", "label": "水餃", "text": "水餃"}},
{"type": "button", "action": {"type": "message", "label": "酸辣湯", "text": "酸辣湯"}}
]
}
}
}

```
send(token, [flex])
```

def reply(token, text):
send(token, [{"type": "text", "text": text}])

def send(token, messages):
headers = {
"Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
"Content-Type": "application/json"
}

```
body = {
    "replyToken": token,
    "messages": messages
}

requests.post(
    "https://api.line.me/v2/bot/message/reply",
    headers=headers,
    json=body
)
```

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
