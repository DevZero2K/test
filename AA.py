import time
import keyboard
from pynput.keyboard import Controller

keyboard_ctrl = Controller()
enabled = False  # Trạng thái ban đầu là tắt

def toggle_tool():
    global enabled
    enabled = not enabled
    print(f"Tool is {'enabled' if enabled else 'disabled'}.")

def press_e():
    keyboard_ctrl.press('e')
    keyboard_ctrl.release('e')

def on_hotkey():
    if enabled:
        press_e()

# Gán phím tắt "Ctrl+Shift+E" để bật/tắt công cụ
keyboard.add_hotkey('Ctrl+Shift+E', toggle_tool)

# Gán phím tắt "Ctrl+Shift+Q" để tắt chương trình
keyboard.add_hotkey('Ctrl+Shift+Q', lambda: keyboard_ctrl.press('esc'))

# Đợi 7 giây trước khi bắt đầu
time.sleep(1)

while True:
    if enabled:
        press_e()
        # Đợi 1 giây trước khi nhấn "e" tiếp theo
        time.sleep(7)
    else:
        time.sleep(0.1)

while True:
    if enabled:
        press_e()
        # Đợi 1 giây trước khi nhấn "e" tiếp theo
        time.sleep(7)
    else:
        time.sleep(0.1)

while True:
    if enabled:
        press_e()
        # Đợi 1 giây trước khi nhấn "e" tiếp theo
        time.sleep(7)
    else:
        time.sleep(0.1)

asdsad
asdasdsadsad
asdasd

asdsad
assertsad
StopAsyncIterationdsa
dsa
d1233333333333333333333333333333333333

sadsad

assertas
assertsad
StopAsyncIterationsad

setdas
dsa

asdsadas
das




Danh lol del thích