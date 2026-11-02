import os
import requests

TARGET_URL = os.environ["TARGET_URL"]
WEBHOOK = os.environ["SLACK_WEBHOOK_URL"]
NO_VACANCY = "空き部屋がございません"
PAGE_MARKER = "利用申込"

def notify(text):
    requests.post(WEBHOOK, json={"text": text}, timeout=10)

def main():
    if os.environ.get("TEST_NOTIFY") == "true":
        notify("テスト通知です")
        return
    r = requests.get(TARGET_URL, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    html = r.text
    if PAGE_MARKER not in html:
        return
    if NO_VACANCY not in html:
        notify(":tada: 空きが出た可能性があります!\n" + TARGET_URL)

if __name__ == "__main__":
    main()
