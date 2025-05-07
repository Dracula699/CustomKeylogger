import keyboard
import time

file_path = "random.txt"
text = ""
set_time = int(input("For how much time should we log ur text(input in seconds): "))

print(f"Start typing... You have {set_time} seconds")

def on_key(event):
    global text
    if event.event_type == 'up':
        if event.name == "space":
            text += " "
        elif event.name == "backspace":
            if len(text) > 0:
                text = text[:-1]
            text = text
        elif len(event.name) == 1:
            text += event.name
        elif event.name == "enter":
            text += '\n'

        with open(file_path, "a+") as file:
            file.write(text)

keyboard.hook(on_key)


time.sleep(set_time)


keyboard.unhook_all()

print("text loged")
