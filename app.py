@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/", methods=["POST"])
def webhook():
    ...
from flask import Flask, request
import requests
import os

app = Flask(**name**)

# 🔑 你的 LINE Token（已幫你放好）

CHANNEL_ACCESS_TOKEN = "XlA2IPfLH7iJYrdyzyQJ4nsO/z2QtvN9KDK5hF4lYSbDXFuBHjjba6RDGboj9b3L5blXJMrgYt8BRjpBxpRE4HEPIpyITY0IqMAuTcvfe1FCoFN309KkIAZosJJcjwUEmVLFDUxqoeLJYbAF5kxmeQdB04t89/1O/w1cDnyilFU="

# 訂單資料（暫存在記憶體）

orders = []

# 菜單

menu = ["鍋貼", "水餃", "酸辣湯"]

@app.route("/", methods=["POST"])
def webhook():
data = request.json

```
for event in data.get("events", []):
    if event["type"] == "message":
        reply_token = event["replyToken"]
        user_id = event["source"].get("userId", "某人")
        msg = event["message"]["text"]

        # 👉 顯示菜單
        if msg == "八方":
            send_bafang_menu(reply_token)

        # 👉 點餐
        elif msg in menu:
            orders.append((user_id, msg))
            reply(reply_token, f"✅ 已點：{msg}")

        # 👉 統計
        elif msg == "統計":
            summary = {}
            for _, item in orders:
                summary[item] = summary.get(item, 0) + 1

            if summary:
                text = "📊 統計結果：\n"
                for k, v in summary.items():
                    text += f"{k}：{v}\n"
            else:
                text = "目前沒人點餐"

            reply(reply_token, text)

        else:
            reply(reply_token, "👉 輸入「八方」開始點餐")

return "OK"
```

# 👉 八方按鈕菜單

def send_bafang_menu(token):
flex = {
"type": "flex",
"altText": "八方雲集菜單",
"contents": {
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🥟 八方雲集",
"weight": "bold",
"size": "xl"
},
{
"type": "button",
"action": {
"type": "message",
"label": "🥟 鍋貼",
"text": "鍋貼"
}
},
{
"type": "button",
"action": {
"type": "message",
"label": "🥟 水餃",
"text": "水餃"
}
},
{
"type": "button",
"action": {
"type": "message",
"label": "🥣 酸辣湯",
"text": "酸辣湯"
}
}
]
}
}
}

```
send(token, [flex])
```

# 👉 回覆訊息

def reply(token, text):
send(token, [{"type": "text", "text": text}])

# 👉 發送訊息

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

# 👉 Render 必備（非常重要）

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
