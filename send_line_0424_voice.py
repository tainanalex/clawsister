import time
from linebot import LineBotApi
from linebot.models import AudioSendMessage
import json

LINE_CHANNEL_ACCESS_TOKEN = "1/zSo34...(redacted)"
USER_ID = "Uecbea6f249d4b84e337808dfe0c36d0b"

direct_url = "https://tmpfiles.org/dl/34962401/2026-04-24_voice.mp3"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# 發送語音訊息（約 28 秒）
message = AudioSendMessage(
    original_content_url=direct_url,
    duration=28000  # 28 秒
)

try:
    line_bot_api.push_message(USER_ID, message)
    print("2026-04-24 語音訊息已發送到 LINE！")
except Exception as e:
    print(f"LINE Bot API Error: {e}")
