import requests
import helpers


SLACK_BOT_OAUTH_TOKEN = helpers.config('SLACK_BOT_OAUTH_TOKEN',default=None,cast=str)

def send_message(message, channel_id=None, user_id=None,thread_ts=None):
    url= "https://slack.com/api/chat.postMessage"
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {SLACK_BOT_OAUTH_TOKEN}',
        "Accept": "application/json"
    }
    if user_id is not None:
        message=f"<@{user_id}> {message}"
    
    data = {
        "channel": f"{channel_id}",
        "text": f"{message}".strip(),
    }
    if thread_ts is not None:
        data["thread_ts"] = thread_ts
    return requests.post(url, headers=headers, json=data)
  

