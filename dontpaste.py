import keyboard
import pyperclip

# Händelsehanterare som lyssnar efter Ctrl+Alt+P
def handle_hotkey():
    text = pyperclip.paste()
    keyboard.write(text)

# Registrera hotkey
keyboard.add_hotkey('ctrl+alt+p', handle_hotkey)

# Fortsätt lyssna efter händelser
keyboard.wait()
