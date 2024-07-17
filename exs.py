import random
import os
import time
import platform
import cv2
import numpy as np

path = 'C:\\Users\\tdbbr\\Documents\\ssss\\sss\\'
screenshot_path = f'{path}screenshot.png'
def get_null_device():
    return 'NUL' if platform.system() == 'Windows' else '/dev/null'
null_device = get_null_device()
def get_locate(icon_path, name_action):
    adb_capture_screenshot()
    # Đọc ảnh chụp màn hình và ảnh mẫu của icon
    screenshot = cv2.imread(screenshot_path)
    icon = cv2.imread(icon_path)

    # Kiểm tra xem ảnh có được đọc thành công hay không
    if screenshot is None:
        print(f"Không thể đọc ảnh từ {screenshot_path}")
        return None, None
    if icon is None:
        print(f"Không thể đọc ảnh từ {icon_path}")
        return None, None

    # Thực hiện so khớp mẫu
    result = cv2.matchTemplate(screenshot, icon, cv2.TM_CCOEFF_NORMED)

    # Thiết lập ngưỡng để xác định vùng có độ tương đồng cao
    threshold = 0.8
    locations = np.where(result >= threshold)

    # Kiểm tra nếu không tìm thấy icon
    if len(locations[0]) == 0:
        print(f"Không tìm thấy {name_action}.")
        return None, None
    # Lấy tọa độ của vùng có độ tương đồng cao nhất
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    center_x = top_left[0] + icon.shape[1] // 2
    center_y = top_left[1] + icon.shape[0] // 2
    # Xuất tọa độ của icon
    print(f"{name_action}")
    return center_x, center_y

def adb_capture_screenshot():
    time.sleep(2)
    os.system(f"adb shell screencap -p /sdcard/screenshot.png > {null_device} 2>&1")
    os.system(f"adb pull /sdcard/screenshot.png {path}screenshot.png > {null_device} 2>&1")

def open_application(package_name):
    command = f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1 > {null_device} 2>&1"
    os.system(command)
    time.sleep(1)
def input_text(text):
    os.system(f"adb shell input text 1")
    press_backspace_multiple_times(1)
    os.system(f"adb shell input text {text}")

def input_key_enter():
    os.system("adb shell input keyevent 66")
def press_backspace_multiple_times(count):
    for _ in range(count):
        os.system("adb shell input keyevent KEYCODE_DEL")
def adb_click(center_x, center_y):
    if center_x is not None and center_y is not None:
        adb_command = f"adb shell input tap {center_x} {center_y}"
        os.system(adb_command)

def swipe_up():
    os.system(f"adb shell input swipe 500 1600 500 400 500")
def swipe_down():
    start_x = random.randint(400, 600)
    start_y = random.randint(300, 600)
    end_x = start_x
    end_y = random.randint(1300, 1600)
    duration = random.randint(200, 700)  # Thời gian vuốt ngẫu nhiên
    os.system(f"adb shell input swipe {start_x} {start_y} {end_x} {end_y} {duration}")

def swipe_check_button(screen_find, number_swipe, name_action):
    num = 0
    while num < number_swipe:
        x, y = get_locate(screen_find, name_action)
        if x is not None and y is not None:
            return x, y
        num += 1
        swipe_up()
        time.sleep(1)
    return None, None
jobs = [
    {'username': 'olgahird+sx1@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowset", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x1.zip'},
    {'username': 'olgahird+sx2@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowses", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x2.zip'},
    {'username': 'olgahird+sx3@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowseu", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x3.zip'},
    {'username': 'olgahird+sx4@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowseq", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x4.zip'},
	{'username': 'olgahird+sx5@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowsez", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x5.zip'},
	{'username': 'olgahird+sx6@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowsey", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x6.zip'},
	{'username': 'olgahird+sx7@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowsex", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x7.zip'},
	{'username': 'olgahird+sx8@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowsev", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x8.zip'},
	{'username': 'olgahird+sx9@gmail.com', "linkapp":"mobi.mgeek.TunnyBrowsew", 'file': 'https://github.com/ThanhVan9721/cz/archive/refs/heads/x9.zip'},
]

count = 0
while True:
    count += 1
    print(f"Thực hiện lần: {count}")
    for job in jobs:
        user_name = job['username']
        file = job['file']
        link_app = job['linkapp']
        open_application(link_app)
        swipe_down()
        url_br = f'{path}btn//urlBr.png'
        center_x, center_y = get_locate(url_br, "Url br")
        adb_click(center_x, center_y)
        input_text('https://tria.ge/submit/file')
        input_key_enter()

        button_next = f'{path}btn//btnNext.png'
        center_x, center_y = get_locate(button_next, "Button Cookies")
        if center_x is not None:
            button_cookies = f'{path}btn//btnCookie.png'
            center_x, center_y = get_locate(button_cookies, "Button Cookies")
            adb_click(center_x, center_y)

            input_login = f'{path}btn//inputLogin.png'
            center_x, center_y = get_locate(input_login, "Button Login")
            adb_click(center_x, center_y)
            input_text(user_name)
            input_key_enter()
            input_text("Buithanhvan1!")
        input_link = f'{path}btn//inputLink.png'
        center_x, center_y = swipe_check_button(input_link, 10, "input_link")
        adb_click(center_x, center_y)
        input_text(file)

        btn_fet = f'{path}btn//btnFet.png'
        center_x, center_y = swipe_check_button(btn_fet, 10, "btn_fet")
        adb_click(center_x, center_y)
        time.sleep(1)
        btn_des = f'{path}btn//btnDes.png'
        center_x, center_y = swipe_check_button(btn_des, 10, "btn_des")
        adb_click(center_x, center_y)

        btn_exe = f'{path}btn//btnExe.png'
        center_x, center_y = swipe_check_button(btn_exe, 10, "btn_exe")
        adb_click(center_x, center_y)

        btn_win_10 = f'{path}btn//btnWin10.png'
        center_x, center_y = swipe_check_button(btn_win_10, 10, "btn_win_10")
        adb_click(center_x, center_y)

        btn_10_p = f'{path}btn//btn10p.png'
        center_x, center_y = swipe_check_button(btn_10_p, 10, "btn_10_p")
        adb_click(center_x, center_y)

        btn_Analy = f'{path}btn//btnAnaly.png'
        center_x, center_y = swipe_check_button(btn_Analy, 10, "btn_Analy")
        adb_click(center_x, center_y)
        time.sleep(1)

    time.sleep(300)