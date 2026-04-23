import time
from linebot import LineBotApi
from linebot.models import AudioSendMessage
import os
import json

LINE_CHANNEL_ACCESS_TOKEN = "1/zSo34..."
USER_ID = "Uecbea6f249d4b84e337808dfe0c36d0b"

# 先上傳到 tmpfiles 取得 URL，然後修改 direct link
audio_file = "D:/clawsister/2026-04-21_voice.mp3"
if not os.path.exists(audio_file):
    print(f"File not found: {audio_file}")
    exit(1)

# 用 curl 上傳並取得 URL
os.system(f"cd D:/clawsister; curl.exe -F 'file=@2026-04-21_voice.mp3' https://tmpfiles.org/api/v1/upload > upload_resp.json")
with open("D:/clawsister/upload_resp.json") as f:
    resp = json.load(f)
tmp_url = resp["data"]["url"]
direct_url = tmp_url.replace("tmpfiles.org", "tmpfiles.org/dl")

print(f"Audio URL: {direct_url}")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# 發送語音訊息（約 25-30 秒）
message = AudioSendMessage(
    original_content_url=direct_url,
    duration=28000  # 28 秒
)

try:
    line_bot_api.push_message(USER_ID, message)
    print("2026-04-21 語音訊息已發送到 LINE！")
except Exception as e:
    print(f"LINE Bot API Error: {e}")
