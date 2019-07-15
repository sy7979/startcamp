import requests
from decouple import config
token = config("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/"
print(url)
user_id = config("CHAT_ID")

# send_url = f"{url}sendmessage?chat_id={user_id}&text=열심히하자"
# requests.get(send_url)

ngrok_url = "https://daramjidotori.pythonanywhere.com/"
webhook_url = f"{url}setwebhook?url={ngrok_url}/{token}"
print(webhook_url)
