from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = "1/zSo34...(redacted)"
USER_ID = "Uecbea6f249d4b84e337808dfe0c36d0b"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

msg = TextSendMessage(
    text="Alex哥～下午六點十分囉！💹✨💃🦞\n\n今天台股V形反轉，大漲1218點，創歷史新高38932！台積電2185元天價，聯發科亮燈漲停2435元！\n\n五大分析師報告已上線：\nhttps://tainanalex.github.io/clawsister/login.html\n密碼：LiLi2516169\n\n🎙️語音因LINE API金鑰過期稍後補發，請Alex哥稍候喔～"
)

try:
    line_bot_api.push_message(USER_ID, msg)
    print("文字訊息已發送到 LINE！")
except Exception as e:
    print(f"LINE Bot API Error: {e}")
