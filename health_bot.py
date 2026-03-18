import feedparser
import subprocess
from datetime import datetime

SIGNAL_NUMBER = "+639XXXXXXXXX"
RECIPIENT = "+639YYYYYYYYY"

feeds = {
"DOH": "https://doh.gov.ph/rss.xml",
"WHO": "https://www.who.int/rss-feeds/news-english.xml",
"UNICEF": "https://www.unicef.org/rss.xml"
}

def get_updates():
    updates = []
    for source, url in feeds.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:1]:
            title = entry.title
            summary = entry.summary[:120] if "summary" in entry else "No summary"
            link = entry.link

            updates.append((title, summary, link))

    return updates

def generate_message():
    date = datetime.now().strftime("%d/%m/%Y")

    msg = f"📢 HEALTH ADVISORY\nDate: {date}\n\n"

    for title, summary, link in get_updates():
        msg += f"Title: {title}\n"
        msg += f"Summary: {summary}...\n"
        msg += f"👉 Click here to see full article:\n{link}\n\n"

    return msg

def send_signal(msg):
    subprocess.run([
        "signal-cli",
        "-u", SIGNAL_NUMBER,
        "send",
        RECIPIENT,
        "-m", msg
    ])

send_signal(generate_message())
