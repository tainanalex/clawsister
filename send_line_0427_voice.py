import time
from linebot import LineBotApi
from linebot.models import AudioSendMessage
import os
import json

LINE_CHANNEL_ACCESS_TOKEN = "1/zSo34..."
USER_ID = "Uecbea6f249d4b84e337808dfe0c36d0b"

# Audio URL from tmpfiles
direct_url = "https://tmpfiles.org/dl/35385941/2026-04-27_voice.mp3"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# 語音訊息
message = AudioSendMessage(
    original_content_url=direct_url,
    duration=38000  # 38 秒
)

try:
    line_bot_api.push_message(USER_ID, message)
    print("2026-04-27 語音訊息已發送到 LINE！")
except Exception as e:
    print(f"LINE Bot API Error: {e}")
