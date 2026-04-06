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
                    {"type": "text", "text": "八方雲集", "weight": "bold", "size": "xl"},
                    {"type": "button",
                     "action": {"type": "message", "label": "🥟 鍋貼", "text": "鍋貼"}},
                    {"type": "button",
                     "action": {"type": "message", "label": "🥟 水餃", "text": "水餃"}},
                    {"type": "button",
                     "action": {"type": "message", "label": "🥣 酸辣湯", "text": "酸辣湯"}}
                ]
            }
        }
    }

    send(token, [flex])